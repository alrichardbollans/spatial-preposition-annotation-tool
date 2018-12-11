from Tkinter import *

import os

from os.path import expanduser

import csv
import uuid
import datetime

class Annotation():
    preposition = 0
    scene = 0
    figure = 0
    ground = 0
    cam_loc = []
    cam_rot = []
    time = 0

    def __init__(self):
        self.id = uuid.uuid4()

    def __str__(self):
        return "["+str(self.scene)+","+str(self.preposition)+"]"

class Application(Frame):

    def createWidgets(self):


        self.winfo_toplevel().title("Annotation Tool")

        self.label0 = Label(self, text='Scene:',font=("Courier", 20))
        self.label0.grid(row=0, sticky=E)
        
        self.scene_variable=StringVar()
        self.scene_variable.set(get_scene_files()[0])

        self.SCENE=apply(OptionMenu, (self, self.scene_variable) + tuple(get_scene_files()))
        self.SCENE.grid(row=0,column=1, columnspan=3)


        self.DD = Entry(self, width = 4,font=("Courier", 20))
        self.DD.grid(row=1, column=1)
        self.DD.insert(0, "DD")
        self.DD.focus_set()
        self.DD.selection_range(0,END)

        self.MM = Entry(self, width = 4,font=("Courier", 20))
        self.MM.grid(row=1, column=2)
        self.MM.insert(0, "MM")


        self.YY = Entry(self, width = 4,font=("Courier", 20))
        self.YY.grid(row=1, column=3,sticky=W)
        self.YY.insert(0, "YYYY")

        self.label1 = Label(self, text="Date of Birth:",font=("Courier", 20))
        self.label1.grid(row=1, sticky=E)

        self.POB = Entry(self,font=("Courier", 20))
        self.POB.grid(row=2, column=1, columnspan=3)

        self.label2 = Label(self, text="Place of Birth:",font=("Courier", 20))
        self.label2.grid(row=2, sticky=E)

        self.native_variable = IntVar()
        self.check_box = Checkbutton(self, variable = self.native_variable,width=5, height=5)

        self.check_box.grid(row=3, column=3,sticky=[W, N])


        self.label3 = Label(self, anchor=W,wraplength = 400, justify=LEFT,text="Please tick if you are NOT a native English speaker",font=("Courier", 20))
        self.label3.grid(row=3,columnspan=3)
        # self.GENDER = Entry(self)
        # self.GENDER.grid(row=3, column=1)



        self.START = Button(self, text="START", fg='blue', command=self.start)
        self.START.grid(row=4, column=0)


        self.QUIT = Button(self, text="QUIT", fg='red', command=self.quit)
        self.QUIT.grid(row=4,column=1)





    def retrieve_user_info(self):
        global user_id
        user_id = uuid.uuid4()
        DOB = self.DD.get()+'/'+self.MM.get()+'/'+self.YY.get()
        date = datetime.datetime.now()
        return [user_id,date,DOB,self.POB.get(),self.native_variable.get()]#,self.GENDER.get()]
    def retrieve_scene_file(self):
        return self.scene_variable.get()
    def retrieve_scene_name(self):

        file = self.retrieve_scene_file()
        return file[:file.find(".blend")]
    def retrieve_task_type(self):
        file = self.retrieve_scene_file()
        return file[file.find("-")+ 1:file.find(".blend")] ### task type is between "-" and ".blend"

    def start(self):
        self.write_user_info()
        self.run_game()
        self.write_annotations(output_path)


    def run_game(self):
        os.system("./scene\ creation/blender/annotation\ scenes/" +self.retrieve_scene_file())

    def write_user_info(self):
        with open(output_path + '/user list.csv', "a+") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.retrieve_user_info())

    def write_annotations(self,output_path):
        ### create list from output of tool
        with open(output_path + '/output.csv', "r+") as f: 
            reader = csv.reader(f)     
            datalist = list( reader )  



        for annotation in datalist:
            an = Annotation()
            an.task = self.retrieve_task_type()
            an.preposition = str(annotation[1])
            an.scene = self.retrieve_scene_name()
            an.figure = str(annotation[0])
            an.ground = str(annotation[2])
            an.cam_loc = str(annotation[4])
            an.cam_rot = str(annotation[5])
            an.time = str(annotation[6])

            ### add annotations to list
            with open(output_path + '/annotation list.csv', "a+") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([an.id,user_id,an.task,an.scene,an.preposition,an.figure,an.ground,an.cam_loc,an.cam_rot,an.time])

        ### delete output from tool

        os.system("rm "+output_path+"/output.csv")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

def dropbox_home():
    from platform import system
    import base64
    import os.path
    _system = system()
    if _system in ('Windows', 'cli'):
        host_db_path = os.path.join(_get_appdata_path(),
                                    'Dropbox',
                                    'host.db')
    elif _system in ('Linux', 'Darwin'):
        host_db_path = os.path.expanduser('~'
                                          '/.dropbox'
                                          '/host.db')
    else:
        raise RuntimeError('Unknown system={}'
                           .format(_system))
    if not os.path.exists(host_db_path):
        raise RuntimeError("Config path={} doesn't exists"
                           .format(host_db_path))
    with open(host_db_path, 'r') as f:
        data = f.read().split()

    return base64.b64decode(data[1])







def get_scene_files():
    files = []
    for filename in os.listdir('scene creation/blender/annotation scenes/'):
        if filename.endswith(".blend"):
            files.append(filename)
    return files



# dropbox_path = dropbox_home()
# output_path = 'test/'
# output_path = dropbox_path + '/data/'
output_path =expanduser("~")
print(output_path)



root = Tk()
app = Application(master=root)

app.mainloop()

root.destroy()