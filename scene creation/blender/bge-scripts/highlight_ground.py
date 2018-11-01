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
def clean_name(obj):
    if '.' in obj.name:
        clean_name = obj.name[:obj.name.find(".")]
    elif '_' in obj.name:
        clean_name = obj.name[:obj.name.find("_")]
    else: 
        clean_name = obj.name
    return clean_name.lower()
    
def list_clean_names(object_list):
    names = []
    for obj in object_list:
        names.append(clean_name(obj))
    return names

if change.positive:

	for obj in main_scene.objects:
		if obj.get('highlight')==True:
			obj.endObject()

		if obj.get('selectedground') == True:

			# obj.color-=x
			obj['selectedground']=False
	### Make list of rigid bodies
	rigid_objects=[]
	for obj in main_scene.objects:
		if "selectedground" in obj.getPropertyNames() and 'highlight' not in obj.name:
			rigid_objects.append(obj)
	#Make list of rigid bodies of which there are at least two
	ground_list = []
	for obj in rigid_objects:
		if list_clean_names(rigid_objects).count(clean_name(obj))>1 and obj['used'] ==False:
			ground_list.append(obj)
		

	gr = random.choice(ground_list) # randomly pick an object
	print("ground = "+ str(gr))
	highlighter_object = scene.addObject(gr.name+"highlightg")

	gr['selectedground']= True
	gr['used'] =True