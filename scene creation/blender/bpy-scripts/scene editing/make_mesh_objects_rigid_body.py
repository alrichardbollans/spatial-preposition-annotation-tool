import bpy

bpy.ops.object.select_by_type(extend=False, type='MESH')

bpy.ops.rigidbody.objects_add(type='ACTIVE')


static_objects = ['floor','ground','wall','wall.001', 'robot','shelf'] # Note that these are special when calculating support - most of the time this is fine, just need to make sure they are active? but not for things like floor or wall, these are just always static, but shelf for example isn't

for obj in bpy.context.scene.objects:
	if obj.rigid_body is None:
		pass
	elif obj.name.lower() in static_objects:
		obj.rigid_body.enabled =False
	else:
		obj.rigid_body.enabled =True




# bpy.ops.rigidbody.object_add()

# bpy.ops.rigidbody.object_settings_copy()