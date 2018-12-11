import bge
#import csv
from mathutils import Vector


cont = bge.logic.getCurrentController()
empty = cont.owner #owner of the controller is the active object (try print(own))
scene = bge.logic.getCurrentScene()
scenes = bge.logic.getSceneList()


main_scene = scene

hover = cont.sensors["hoverAny"]

leftClick = cont.sensors["leftClick"]
rightClick = cont.sensors["rightClick"] 
deselect = cont.sensors["deselect"]

x=Vector([0.1,2,0.1,0.1])
y=Vector([2,0.1,0.1,0.1]) 


### Select Figure Task

if 'sg' in empty.getPropertyNames():

	if deselect.positive:
		for obj in main_scene.objects:
			if obj.get('selectedground')==True:
				obj.color-=y
				obj['selectedground']=False

	if leftClick.positive: 
		if hover.positive:
			for hit_obj in main_scene.objects:
				if hover.hitObject == hit_obj:
					for obj in main_scene.objects:
						if obj.get('selectedground')==True:
							obj.color-=y
							obj['selectedground']=False


					hit_obj['selectedground']= True
					hit_obj.color += y

					break

### Select Figure Task
if 'sf' in empty.getPropertyNames():

	if deselect.positive:
		for obj in main_scene.objects:
			if obj.get('selectedfigure')==True:
				obj.color-=x
				obj['selectedfigure']=False

	if leftClick.positive: 
		if hover.positive:
			for hit_obj in main_scene.objects:
				if hover.hitObject == hit_obj:
					for obj in main_scene.objects:
						if obj.get('selectedfigure')==True:
							obj.color-=x
							obj['selectedfigure']=False


					hit_obj['selectedfigure']= True
					hit_obj.color += x

					break

### Standard and Select Figure and Ground
if 's' in empty.getPropertyNames() or 'sfg' in empty.getPropertyNames():
	
	if deselect.positive:
		for obj in main_scene.objects:
			if obj.get('selectedfigure')==True:
				obj.color-=x
				obj['selectedfigure']=False
			if obj.get('selectedground')==True:	
				obj.color-=y
				obj['selectedground']=False

	if leftClick.positive: 
		if hover.positive:
			for hit_obj in main_scene.objects:
				if hover.hitObject == hit_obj:
					for obj in main_scene.objects:
						if obj.get('selectedfigure')==True:
							obj.color-=x
							obj['selectedfigure']=False


					hit_obj['selectedfigure']= True
					hit_obj.color += x

					break

	if rightClick.positive:
		if hover.positive:
			for hit_obj in main_scene.objects:
				if hover.hitObject == hit_obj:
					for obj in main_scene.objects:
						if obj.get('selectedground')==True:
							obj.color-=y
							obj['selectedground']=False


					hit_obj['selectedground']= True
					hit_obj.color += y

					break




