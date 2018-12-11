import sys

import os

module_path1 = os.getcwd() + '/add ons/'
module_path2 = os.getcwd() + '/scenes/add ons/'
# So we can add ons
sys.path.append(module_path1)
sys.path.append(module_path2)

import bpy
import blender_utils

scene = bpy.context.scene

for obj in scene.objects:
    #print(obj)
    if obj.rigid_body is None or blender_utils.clean_name(obj) == 'floor':
        pass
    else:
        obj.rigid_body.collision_shape = 'MESH'
        obj.rigid_body.collision_margin = 0.001


        # if obj.rigid_body.use_margin == True:

        #     if obj.rigid_body.collision_margin == 0:
        #         obj.rigid_body.collision_margin = 0.001
        # if obj.rigid_body.use_margin == False:
        #     obj.rigid_body.use_margin = True
            
        #     obj.rigid_body.collision_margin = 0.001

        # obj.rigid_body.angular_damping = 0.8
        # obj.rigid_body.linear_damping = 0.9
        obj.rigid_body.use_deactivation = True
        obj.rigid_body.use_start_deactivated = False
        obj.rigid_body.deactivate_linear_velocity = 0.04
        obj.rigid_body.deactivate_angular_velocity = 0.1

        # obj.collision.stickiness = 0.5

        # bpy.ops.object.select_all(action='DESELECT')

        # obj.select = True

        # bpy.context.scene.objects.active = obj
        # bpy.ops.object.modifier_remove(modifier="Collision")

        #bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')


    # if obj.name == 'Ground' or obj.name == 'Plane':
    # 	obj.rigid_body = True
    # 	obj.rigid_body.enabled = False

            