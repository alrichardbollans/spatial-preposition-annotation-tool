
import bge
import math
import random


preposition_list = ['in','inside','on', 'on top of', 'against', 'over', 'under', 'above','below']

random_preposition_list = preposition_list

random.shuffle(random_preposition_list)

# Makes game run in full screen
# bge.render.setFullScreen(True)

# print(bge.render.getDisplayDimensions())
# print(bge.render.getDisplayDimensions()[0])

bge.render.setWindowSize(1000,700)

cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object (try print(own))
scene = bge.logic.getCurrentScene()

empty = scene.objects['Empty']
empty["random_preposition_list"] = random_preposition_list


scenes = bge.logic.getSceneList()
main_scene = scenes[0]

if 'pragmatic' not in empty.getPropertyNames():
	#### Give camera random starting position
	camera = main_scene.objects['Camera']
	if 'scene1.blend' in empty.getPropertyNames():

		x= random.uniform(-4.4,6.4)

		if x < 1:
			y = random.uniform(-3.4,0)
		else:
			y = random.uniform(-3.4,6.4)



		camera.worldPosition = [x,y,1.8]

	if 'scene2.blend' in empty.getPropertyNames() or 'scene3.blend' in empty.getPropertyNames():

		x= random.uniform(-5.9,4.4)

		if x < 0:
			y = random.uniform(-4.4,-1)
		else:
			y = random.uniform(-4.4,4.9)



		camera.worldPosition = [x,y,1.8]

	### Make it point at centre point
	if 'scene1.blend' in empty.getPropertyNames():
		centre_point = [-1.6,3]
	if 'scene2.blend' in empty.getPropertyNames() or 'scene3.blend' in empty.getPropertyNames():
		centre_point = [-4,3.4]

	xyz = camera.worldOrientation.to_euler()
	xyz[0]= math.radians(90)
	xyz[1] = math.radians(0)

	if x < centre_point[0]:
		rot_z = math.atan((centre_point[1]-y)/(centre_point[0]-x)) - math.radians(90)
	if x > centre_point[0]:
		if y < centre_point[1]:
			rot_z = math.radians(90)+math.atan((centre_point[1]-y)/(centre_point[0]-x))
		elif y > centre_point[1]: 
			rot_z = math.atan((centre_point[1]-y)/(centre_point[0]-x))-math.radians(270)


	if x == centre_point[0]:
		if y < centre_point[1]:
			rot_z = 0
		else:
			rot_z = math.radians(-180)
	if y == centre_point[1]:
		if x < centre_point[1]:
			rot_z = math.radians(-90)
		else:
			rot_z = math.radians(90)

	xyz[2]= rot_z
	camera.worldOrientation = xyz.to_matrix()

bge.logic.sendMessage("change") # start message needed for highlighting
# bge.logic.sendMessage("changepreposition")
# print(scene.objectsInactive)

# Tags all highlighter objects as 'highlights'
for obj in scene.objectsInactive:

	obj['highlight'] = True





# preposition_objects = []
# for objs in preposition_overlay_scene.objects:
# 	print(obj.name + str(obj.getPropertyNames()))
# 	if "preposition" in obj.getPropertyNames():
# 		preposition_objects.append(obj)
# 		obj['selectedprep'] = False
# preposition_objects[0]['selectedprep'] = True
