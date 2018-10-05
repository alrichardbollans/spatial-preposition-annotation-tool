import bpy
scene = bpy.context.scene

for obj in scene.objects:
    #print(obj)
    if obj.rigid_body is None:
        pass
    else:
        obj.select = True

        bpy.context.scene.objects.active = obj
        bpy.ops.transform.translate(value=(0, -0.0001, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
