import bge
#import csv
from mathutils import Vector


cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object (try print(own))
scene = bge.logic.getCurrentScene()
scenes = bge.logic.getSceneList()

main_scene = scene
preposition_overlay_scene = scenes[1]

hover = cont.sensors["MouseOver"]
leftClick = cont.sensors["leftClick"]
rightClick = cont.sensors["rightClick"] 
deselect = cont.sensors["deselect"]

x=Vector([0.1,2,0.1,0.1])
y=Vector([2,0.1,0.1,0.1]) 

if deselect.positive:
	if own['selectedfigure']==True:
		own.color-=x
		own['selectedfigure']=False
	if own['selectedground']==True:	
		own.color-=y
		own['selectedground']=False
	# triple=[0,1,2]
		
if leftClick.positive: 
	if hover.positive:
		for obj in main_scene.objects:
			if obj.get('selectedfigure')==True:
				obj.color-=x
				obj['selectedfigure']=False


		own['selectedfigure']= True
		own.color += x

if rightClick.positive:
	if hover.positive:
		for obj in main_scene.objects:
			if obj.get('selectedground')==True:	
				obj.color-=y
				obj['selectedground']=False
		own['selectedground']= True
		own.color += y


# triple=[0,1,2]

# for obj in main_scene.objects:
	
# 	if obj.get('selectedfigure')==True:
# 		triple[0]=obj

# 	if obj.get('selectedground')==True:	
# 		triple[2] = obj
		


# for obj in preposition_overlay_scene.objects:
# 	if obj.get('selectedprep')==True:
# 		triple[1]=obj

# if triple[0] != 0 and triple[1] != 1 and triple[2] != 2:
	
# 	bge.logic.sendMessage("deselect") #Sends a deselect message to sensors in any active scene.

# 	print(triple)
# 	triple.append("currentscene")
# 	with open('output.csv', "a") as csvfile:
# 		outputwriter = csv.writer(csvfile)
# 		outputwriter.writerow(triple)

# 	cam_loc = scene.objects["Camera"].position
# 	cam_rot = scene.objects["Camera"].orientation
# 	print(cam_loc)
# 	print(cam_rot)

# 	for obj in preposition_overlay_scene.objects:
# 		obj['selectedprep']=False
			

