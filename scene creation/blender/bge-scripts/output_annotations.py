import bge
import csv


cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object (try print(own))
scene = bge.logic.getCurrentScene()
scenes = bge.logic.getSceneList()
deselect = cont.sensors["deselect"]


if len(scenes) == 2:
	main_scene = scene
	preposition_overlay_scene = scenes[1]

	triple=[0,1,2]

	for obj in main_scene.objects:
		
		if obj.get('selectedfigure')==True:
			triple[0]=obj

		if obj.get('selectedground')==True:	
			triple[2] = obj

	for obj in preposition_overlay_scene.objects:
		if obj.get('selectedprep')==True:
			triple[1]=obj

	if triple[0] != 0 and triple[1] != 1 and triple[2] != 2:
		bge.logic.sendMessage("deselect") #Sends a deselect message to sensors in any active scene.

		print(triple)
		triple.append("currentscene")
		with open('output.csv', "a") as csvfile:
			outputwriter = csv.writer(csvfile)
			outputwriter.writerow(triple)

		cam_loc = scene.objects["Camera"].position
		cam_rot = scene.objects["Camera"].orientation
		print(cam_loc)
		print(cam_rot)

		for obj in preposition_overlay_scene.objects:
			obj['selectedprep']=False
				
	if deselect.positive:
		triple=[0,1,2]
else:
	pass