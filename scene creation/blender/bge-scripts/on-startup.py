
import bge
cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object (try print(own))
scene = bge.logic.getCurrentScene()

scenes = bge.logic.getSceneList()
main_scene = scenes[0]


bge.logic.sendMessage("change") # start message needed for highlighting
bge.logic.sendMessage("changepreposition")
# print(scene.objectsInactive)

for obj in scene.objectsInactive:

	obj['highlight'] = True


# preposition_objects = []
# for objs in preposition_overlay_scene.objects:
# 	print(obj.name + str(obj.getPropertyNames()))
# 	if "preposition" in obj.getPropertyNames():
# 		preposition_objects.append(obj)
# 		obj['selectedprep'] = False
# preposition_objects[0]['selectedprep'] = True
