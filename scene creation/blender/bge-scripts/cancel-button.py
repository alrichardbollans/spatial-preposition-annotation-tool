import bge
cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object (try print(own))
scene = bge.logic.getCurrentScene() #this sets scene as a bge.types.KX_Scene object



hover = cont.sensors["MouseOver"]
leftClick = cont.sensors["leftClick"] #note leftclick shold be set to 'tap'(?)


if leftClick.positive and hover.positive:


	bge.logic.sendMessage("deselect") #Sends a deselect message to sensors in any active scene.
	bge.logic.sendMessage("change")
	bge.logic.sendMessage("changepreposition")
