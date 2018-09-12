import bge
cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object (try print(own))
scene = bge.logic.getCurrentScene() #this sets scene as a bge.types.KX_Scene object



hover = cont.sensors["MouseOver"]
leftClick = cont.sensors["leftClick"] #note leftclick shold be set to 'tap'(?)
deselect = cont.sensors["deselect"]


if leftClick.positive and hover.positive:
	triple =[0,own,0]
	
	for obj in bpy.data.scenes["Scene"]:
		if obj["selectedfigure"] == True:
			triple[0]=obj
		if obj["selectedground"] == True:
			triple[2]=obj
	bge.logic.sendMessage("change")
	
	with open('output.csv', "a") as csvfile:
		outputwriter = csv.writer(csvfile)
		outputwriter.writerow(triple)

if deselect.positive:
	own['selectedprep']= False
	for child in own.children:
		child.color = (1,1,1,1)
