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
        obj.collision.stickiness = 0.5