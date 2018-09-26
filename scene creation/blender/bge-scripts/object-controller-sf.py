import bge
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

if deselect.positive:
	if own['selectedfigure']==True:	
		own.color-=x
		own['selectedfigure']=False
	# triple=[0,1,2]


if leftClick.positive:
	if hover.positive:
		for obj in main_scene.objects:
			if obj.get('selectedfigure')==True:
				obj.color-=x
				obj['selectedfigure']=False

		own['selectedfigure']= True
		own.color += x