import bge
cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object (try print(own))
scene = bge.logic.getCurrentScene()
menuOverlay=bge.logic.addScene("Scene.001", 1) # need to change to add scene on boot

