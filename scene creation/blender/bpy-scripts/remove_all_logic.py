### script for removing all logic and properties in both scenes and also unlinking scripts
### Doesn't like invisible objects?!

import bpy 

def remove_logic(scene):
	bpy.context.screen.scene = scene
	for obj in scene.objects:
		obj.select = True

		bpy.context.scene.objects.active = obj
		
		#bpy.ops.object.game_property_clear()

		for sens in obj.game.sensors:
			bpy.ops.logic.sensor_remove(sensor=sens.name, object=obj.name)

		for cons in obj.game.controllers:
			bpy.ops.logic.controller_remove(controller=cons.name, object=obj.name)


		for acts in obj.game.actuators:
			bpy.ops.logic.actuator_remove(actuator=acts.name, object=obj.name)

		obj.select = False


for scene in bpy.data.scenes:
	remove_logic(scene)


### Unlink texts
texts_to_keep_linked = ["add_logic_in_blender.py","remove_all_logic.py", "edit_rendering.py"]
for txts in bpy.data.texts:
	if txts.name not in texts_to_keep_linked:
		bpy.data.texts.remove(txts)

