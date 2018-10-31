### Script that runs continuously with an always sensor in an Empty object
### Note this uses RED and BLUE wireframe to highlight objects => don't use red as a color for objects
### idea is to create a copy of object
# with separate material 
# remove texture 
# set diffuse color and wire render
# remove object color  and use mistfrom opitons
import bge
import random


scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object

scenes = bge.logic.getSceneList()

main_scene = scene

change = cont.sensors["change"]


if change.positive:

	for obj in main_scene.objects:
		if obj.get('highlight')==True:
			obj.endObject()

	rigid_objects=[]
	for obj in main_scene.objects:
		if "selectedground" in obj.getPropertyNames() and 'highlight' not in obj.name:
			rigid_objects.append(obj)

	for obj in rigid_objects:
		if obj.get('selectedground') == True:

			# obj.color-=x
			obj['selectedground']=False

	ground = random.choice(rigid_objects) # randomly pick an object
	print("ground = "+ ground.name)
	highlighter_object = scene.addObject(ground.name+"highlightg")

	ground['selectedground']= True