import bpy

import blender_utils

scene = bpy.context.scene

weights={'pencil':0.01, 
		'spoon': 0.05, 
		'bowl': 0.3,
		'cube': 0.1, 
		'apple': 0.05,
		'banana': 0.05, 
		'robot': 20, 
		'book': 0.3, 
		'bookshelf': 10
             }

for obj in scene.objects:
	if obj.rigid_body is None:
	    pass
	elif blender_utils.clean_name(obj) in weights:
		obj.rigid_body.mass = weights[blender_utils.clean_name(obj)]
