import bpy

import blender_utils

scene = bpy.context.scene

list_objs = []

for obj in scene.objects:
	if 'highlight' not in obj.name:
		list_objs.append(obj)

print(len(list_objs))