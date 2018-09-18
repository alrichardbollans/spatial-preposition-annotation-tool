### Script that runs continuously with an always sensor in an Empty object in the overlay scene

import bge


scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object

scenes = bge.logic.getSceneList()

preposition_overlay_scene = scene

# names_of_unrigid_objects = ["Camera","Lamp","Empty","__default__cam__","Hemi","Hemi.001","Sun"]
# rigid_objects=[]
# for obj in scene.objects:
	
# 	if obj.name not in names_of_unrigid_objects:
# 		rigid_objects.append(obj)

change = cont.sensors["changepreposition"]
preposition_objects = []

for obj in preposition_overlay_scene.objects:
	if "preposition" in obj.getPropertyNames():
		preposition_objects.append(obj)



for obj in preposition_objects:
	if obj.get('selectedprep') == True:
		for child in obj.children:
			child.color = (1,1,1,1)

	if obj.get('selectedprep') == False:
		for child in obj.children:
			child.color = (1,1,1,0)

if change.positive: #Cycles through prepositions
	if all(obj['selectedprep'] == False for obj in preposition_objects):
		preposition_objects[0]['selectedprep'] = True
	else:

		for obj in preposition_objects:
			if obj.get('selectedprep') == True:
				print(obj.name)
				obj['selectedprep'] = False
				new_index = preposition_objects.index(obj) + 1
				if new_index < len(preposition_objects):
					preposition_objects[new_index]['selectedprep'] = True
				else:
					preposition_objects[0]['selectedprep'] = True
				break
















