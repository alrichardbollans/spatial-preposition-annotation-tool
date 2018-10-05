### Handles with textual displays and input as well as output

import sys

# So we can find the bgui module
sys.path.append('../..')

import csv
import random

import bgui
import bgui.bge_utils
import bge



main_scene = bge.logic.getCurrentScene()

co = bge.logic.getCurrentController()
empty = co.owner


keyboard = co.sensors["textinputkeyboard"]

### This allows users to reset choices and replaces the old cancel button

for key,status in keyboard.events:
    if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
        if key == bge.events.DELKEY:
            bge.logic.sendMessage("deselect") #Sends a deselect message to sensors in any active scene.
            bge.logic.sendMessage("change")

preposition_list = ['in','on','over','near','above','to the left of', 'to the right of', 'against']

class SimpleLayout(bgui.bge_utils.Layout):
    """A layout showcasing various Bgui features"""

    def __init__(self, sys, data):
        super().__init__(sys, data)
        
        #Use a frame to store all of our widgets
        self.frame = bgui.Frame(self, border=0)
        self.frame.colors = [(0, 0, 0, 0) for i in range(4)]


        

        # Add a label for the title
        self.lbl = bgui.Label(self, text=empty.getPropertyNames()[0], pos=[0, .95],
            sub_theme='Large', options = bgui.BGUI_DEFAULT | bgui.BGUI_CENTERX) 

        if "p" not in empty.getPropertyNames():
            # A label for the given preposition
            self.lbl2 = bgui.Label(self, text= preposition_list[0], pos=[0, 0.9],
                sub_theme='Large', options = bgui.BGUI_DEFAULT | bgui.BGUI_CENTERX)          


        
        if "p" in empty.getPropertyNames():
            # A themed frame to store widgets
            self.win = bgui.Frame(self,  size=[.6, .1],pos=[0, 0.1],border=0.2,
                options=bgui.BGUI_DEFAULT|bgui.BGUI_CENTERX)

            self.lbl2 = bgui.Label(self, text="You've entered: ", pos=[0, 0.9],
                sub_theme='Large', options = bgui.BGUI_DEFAULT | bgui.BGUI_CENTERX)

            # A TextInput widget
            self.input = bgui.TextInput(self.win, text="",
                input_options = 1, options = bgui.BGUI_DEFAULT)
            self.input.activate()
            self.input.on_enter_key = self.on_input_enter


    def on_input_enter(self, widget):
        self.lbl2.text = "You've entered: " + widget.text

        
        bge.logic.sendMessage("deselect") #Sends a deselect message to sensors in any active scene.
        bge.logic.sendMessage("change")

        triple=[0,1,2]

        triple[1]=widget.text

        main_scene = bge.logic.getCurrentScene()

        for obj in main_scene.objects:
            
            if obj.get('selectedfigure')==True:
                triple[0]=obj

            if obj.get('selectedground')==True: 
                triple[2] = obj

        print(str(triple))
        triple.append("currentscene")

        cam_loc = main_scene.objects["Camera"].position
        cam_rot = main_scene.objects["Camera"].orientation
        triple.append(cam_loc)
        triple.append(cam_rot)

        with open('output.csv', "a") as csvfile:
            outputwriter = csv.writer(csvfile)
            outputwriter.writerow(triple)

        

        widget.text = ""
        #widget.deactivate()
        #widget.frozen = 1
        
    # def on_img_click(self, widget):
    #     self.counter += 1
    #     self.lbl.text = "You've clicked me %d times" % self.counter
    #     self.progress.percent += .1
    #     if self.counter % 2 == 1:
    #         self.win.img.texco = [(1,0), (0,0), (0,1), (1,1)]
    #     else:
    #         self.win.img.texco = [(0,0), (1,0), (1,1), (0,1)]


def main(cont):
    own = cont.owner
    mouse = bge.logic.mouse

    if 'sys' not in own:
        # Create our system and show the mouse
        own['sys'] = bgui.bge_utils.System('../../themes/default')
        own['sys'].load_layout(SimpleLayout, None)
        mouse.visible = True

    else:
        own['sys'].run()



main(bge.logic.getCurrentController())

### Things that need to run constantly
if "p" in empty.getPropertyNames():
    co.owner['sys'].layout.input.system.focused_widget = co.owner['sys'].layout.input

if "p" not in empty.getPropertyNames():
    #### Output annotations
    triple=[0,1,2]
    triple[1] = co.owner['sys'].layout.lbl2.text
    for obj in main_scene.objects:
        
        if obj.get('selectedfigure')==True:
            triple[0]=obj

        if obj.get('selectedground')==True: 
            triple[2] = obj

    if triple[0] != 0 and triple[1] != 1 and triple[2] != 2:
        bge.logic.sendMessage("deselect") #Sends a deselect message to sensors in any active scene.

        print(triple)
        triple.append("currentscene")

        cam_loc = main_scene.objects["Camera"].position
        cam_rot = main_scene.objects["Camera"].orientation
        triple.append(cam_loc)
        triple.append(cam_rot)

        with open('output.csv', "a") as csvfile:
            outputwriter = csv.writer(csvfile)
            outputwriter.writerow(triple)


    #### Change preposition
    changeprep = co.sensors["changepreposition"]

    for key,status in keyboard.events:
        # key[0] == bge.events.keycode, key[1] = status
        if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
            if key == bge.events.SPACEKEY:
                bge.logic.sendMessage("changepreposition")

    if changeprep.positive:
        co.owner['sys'].layout.lbl2.text = random.choice(preposition_list)
        # new_index = preposition_list.index(co.owner['sys'].layout.lbl2.text) + 1

        # if new_index < len(preposition_list):

        #     co.owner['sys'].layout.lbl2.text = preposition_list[new_index]
        # else:
        #     co.owner['sys'].layout.lbl2.text = preposition_list[0]






