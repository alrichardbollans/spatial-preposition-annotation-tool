### Script that runs continuously with an always sensor in an Empty object in the overlay scene

import bge


scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object

scenes = bge.logic.getSceneList()

preposition_overlay_scene = scene



change = cont.sensors["changepreposition"]





for obj in preposition_overlay_scene.objects:
	if "preposition" in obj.getPropertyNames():
		if obj.get('selectedprep') == True:
			for child in obj.children:
				child.color = (1,1,1,1)

		if obj.get('selectedprep') == False:
			for child in obj.children:
				child.color = (1,1,1,0)

if change.positive: #Cycles through prepositions
	preposition_objects = []

	for obj in preposition_overlay_scene.objects:
		if "preposition" in obj.getPropertyNames():
			preposition_objects.append(obj)

	if all(obj['selectedprep'] == False for obj in preposition_objects):
		preposition_objects[0]['selectedprep'] = True

	
	else:
		for obj in preposition_objects:
			if obj.get('selectedprep') == True:
				obj['selectedprep'] = False
				new_index = preposition_objects.index(obj) + 1
				if new_index < len(preposition_objects):

					preposition_objects[new_index]['selectedprep'] = True
				else:
					preposition_objects[0]['selectedprep'] = True

				break















