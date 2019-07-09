import sys

import os

module_path1 = os.getcwd() + '/add ons/'
module_path2 = os.getcwd() + '/scenes/add ons/'
# So we can find the bgui module
sys.path.append(module_path1)
sys.path.append(module_path2)

###TO DO
## 
## Need to get a crude volume measure e.g. span
import bpy



import csv


import blender_utils
from entity import Entity

from mathutils import Vector

project_path = blender_utils.get_project_directory()
output_path = project_path +'/property extraction/blender data/'
relationship_class_path = project_path + '/property extraction/'

sys.path.append(relationship_class_path)

from relationship import Relationship
from relationship import Property

scene = bpy.data.scenes['Scene']

rigid_body_list = blender_utils.create_list_rigid_bodies()

### Creates python object with various attributes relating to geometry of object in scene
def bounds(obj, local=False):

    local_coords = obj.bound_box[:]
    om = obj.matrix_world

    if not local:    
        worldify = lambda p: om * Vector(p[:]) 
        coords = [worldify(p).to_tuple() for p in local_coords]
    else:
        coords = [p[:] for p in local_coords]

    rotated = zip(*coords[::-1])

    push_axis = []
    for (axis, _list) in zip('xyz', rotated):
        info = lambda: None
        info.max = max(_list)
        info.min = min(_list)
        info.distance = info.max - info.min
        push_axis.append(info)

    import collections

    originals = dict(zip(['x', 'y', 'z'], push_axis))

    o_details = collections.namedtuple('object_details', 'x y z')
    return o_details(**originals)


### Calculates simulation
def bake_simulation():
    #### Animation Settings
    bpy.ops.ptcache.free_bake_all()

    scene.rigidbody_world.point_cache.frame_start = 1
    scene.rigidbody_world.point_cache.frame_end = 51

    bpy.ops.ptcache.bake_all(bake=True)

base_movements = {}
cobb_movements = {}
top_movements = {}

def find_base_movement():

    bpy.context.scene.render.engine = 'BLENDER_RENDER'


    ### Create simulation
    bake_simulation()

    for figure in rigid_body_list:
        ##### Initial Position

        #print('Pre-move:')
        bpy.context.scene.frame_set(0)


        object_details = bounds(figure)

        ### lowest point in z-axis
        z_min_initial = object_details.z.min
        z_max_initial = object_details.z.max
        cobb_initial = blender_utils.get_bbox_centre(figure)[2]
        ###### End Position

        bpy.context.scene.frame_set(50)
        floating_objects = ['balloon']
        #print('Post-move:')
        if blender_utils.clean_name(figure) in floating_objects:
            z_min_end = z_min_initial
            z_max_end = z_max_initial
            cobb_end = cobb_initial
        else:
            object_details = bounds(figure)

            ### lowest point in z-axis
            z_min_end = object_details.z.min
            z_max_end = object_details.z.max
            cobb_end = blender_utils.get_bbox_centre(figure)[2]
        ### Results

        z_min_change = round(z_min_initial - z_min_end ,4)
        z_max_change = round(z_max_initial - z_max_end ,4)
        cobb_change = round(cobb_initial - cobb_end,4)

        base_movements[figure.name] = z_min_change
        top_movements[figure.name] = z_max_change
        cobb_movements[figure.name] = cobb_change
        if z_max_change > 0.5:
            print('Warning: ' + figure.name + ' moves ' + str(z_max_change))
    
find_base_movement() 
scene_name = bpy.path.basename(bpy.context.blend_data.filepath)

for obj in rigid_body_list:
    p = Property(scene_name,obj.name)
    p.set_of_properties['base_movement:top'] = top_movements[obj.name]
    p.set_of_properties['base_movement:cobb'] = cobb_movements[obj.name]
    p.set_of_properties['base_movement:bottom'] = base_movements[obj.name]
    p.save_to_csv(output_path)
  