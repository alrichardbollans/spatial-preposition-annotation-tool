import bpy
scene = bpy.context.scene

for obj in scene.objects:
    #print(obj)
    if obj.rigid_body is None:
        pass
    else:

        obj.rigid_body.angular_damping = 0.8
        obj.rigid_body.linear_damping = 0.9
        obj.rigid_body.use_deactivation = True
        obj.rigid_body.use_start_deactivated = False
        obj.rigid_body.deactivate_linear_velocity = 0.4
        obj.rigid_body.deactivate_angular_velocity = 0.4

        obj.collision.stickiness = 0.5

        bpy.ops.object.select_all(action='DESELECT')

        obj.select = True

        bpy.context.scene.objects.active = obj
        bpy.ops.object.modifier_remove(modifier="Collision")

        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')


    if obj.name == 'Ground' or obj.name == 'Plane':
    	obj.rigid_body = True
    	obj.rigid_body.enabled = False