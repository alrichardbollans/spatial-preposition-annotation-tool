import bpy

import blender_utils

scene = bpy.context.scene

# bpy.ops.object.mode_set(mode='EDIT')

# bpy.ops.mesh.select_all(action='SELECT')

# bpy.ops.mesh.remove_doubles()

objects_to_not_clean = ['robot','balloon', 'guitar','folder', 'picture', 'screen', 'keyboard', 'mouse']

for obj in scene.objects:
	if obj.type == 'MESH' and 'highlight' not in obj.name and blender_utils.clean_name(obj) not in objects_to_not_clean:
		bpy.ops.object.mode_set(mode='OBJECT')

		bpy.ops.object.select_all(action='DESELECT')
		obj.select = True

		bpy.context.scene.objects.active = obj

		bpy.ops.object.mode_set(mode='EDIT')
		print (obj.name)

		bpy.ops.mesh.select_all(action='SELECT')

		bpy.ops.mesh.remove_doubles()



