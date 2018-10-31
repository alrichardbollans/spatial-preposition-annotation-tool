import bge

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object

scenes = bge.logic.getSceneList()

main_scene = scene

timer = main_scene.objects['timer']
empty = main_scene.objects['Empty']
seconds = empty['game_time']

m, s = divmod(seconds, 60)

timer.text = "%d:%02d" % (m, s)
