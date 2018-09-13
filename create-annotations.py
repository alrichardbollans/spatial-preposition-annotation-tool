import os
import csv
import uuid



class Annotation():
	preposition = 0
	scene = 0
	figure = 0
	ground = 0
	cam_loc = []
	cam_rot = []

	def __init__(self):
		self.id = uuid.uuid4()
	def __str__(self):
		return "["+str(self.scene)+","+str(self.preposition)+"]"

#x= raw_input("What is the number of the scene you would like to annotate?") #set x to be random integer within range of files
#task_type = raw_input("What kind of task would you like to do? s = Standard annotation task, hfg = Task where a figure and ground is given and preposition must be selected")
sceneinput = raw_input("Which scene file would you like to annotate? (Only the file name is necessary, not the path)") #"scene"+str(x)+"-"+task_type+".blend"
if ".blend" in sceneinput:
	scenefile = sceneinput
	scene = scenefile[:scenefile.find(".blend")]
else:
	scene = sceneinput
	scenefile = sceneinput + ".blend"

task_type = scenefile[scenefile.find("-")+ 1:scenefile.find(".blend")] ### task type is between "-" and ".blend"

### run annotation game

os.system("./scene\ creation/blender/annotation\ scenes/" +str(scenefile)) 

### create list from output of tool
with open('output.csv', "r+") as f: 
	reader = csv.reader(f)     
	datalist = list( reader )  



for annotation in datalist:
	an = Annotation()
	an.task = str(task_type)
	an.preposition = str(annotation[1])
	an.scene = scene
	an.figure = str(annotation[0])
	an.ground = str(annotation[2])

	### add annotations to list
	with open('outputs/annotation list.csv', "a+") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([an.task,an.scene,an.preposition,an.figure,an.ground])

### delete output from tool

os.system("rm output.csv")







# for instance in datalist:
# 	if instance.scene == "currentscene":
# 		instance.scene = "undefined scene"

# f = open('/scenes/output.csv', "r+")
# if csv[3] == "currentscene":
# 	csv[3] = "undefined scene"


# f = open('/scenes/output.csv', "r+")
# if csv[3] == "currentscene":
# 	csv[3] = scenefile