### blender_utils file should be in blender add ons directory. Usually .config/blender/2.79/scripts/addons

import bpy
import os

from mathutils import Vector

scene1_rigid_bodies = ['Pencil.001', 'box.003', 'wall.003', 'wall.002', 'lamp.001', 'apple.003', 'light', 'Pencil.005', 'jar.001', 'Cube.001', 'box.002', 'box.001', 'box', 'spoon.002', 'balloon.001', 'ceiling', 'book.002', 'chair.003', 'chair.002', 'window.002', 'bin', 'guitar', 'chair.001', 'spoon.001', 'spoon', 'folder', 'Picture_001', 'apple.002', 'apple.001', 'Cube', 'Pencil.004', 'book.001', 'Pencil.003', 'book', 'wall.001', 'wall', 'shelf', 'lamp', 'jar', 'Pencil', 'plate', 'mug', 'bowl_001', 'Robot', 'dish', 'table', 'chair', 'cup', 'Table', 'chest', 'Floor']
scene2_rigid_bodies = ['wall.003', 'banana.000', 'Cube.000', 'book.002', 'mug.002', 'notepad_001', 'light', 'book.001', 'book', 'wall.002', 'ceiling', 'bookshelf', 'box.001', 'spoon.001', 'Cube.002', 'Cube.001', 'box', 'chair.001', 'apple.008', 'window', 'door', 'apple.006', 'dish.001', 'jar.001', 'notebook.001', 'banana.004', 'spoon', 'Pencil.003', 'mug.001', 'folder', 'notebook', 'paper.002', 'table.001', 'ball.001', 'wall.001', 'wall', 'shelf', 'Pencil.001', 'ball', 'lamp', 'jar', 'mug', 'bowl_001', 'Robot', 'chair', 'cup', 'Table', 'Floor']
scene3_rigid_bodies = ['wall.003', 'book.002', 'mug.002', 'notepad_001', 'light', 'book.001', 'book', 'wall.002', 'ceiling', 'bookshelf', 'box.001', 'spoon.001', 'Cube.002', 'Cube.001', 'apple.000', 'box', 'chair.001', 'pear.004', 'apple.009', 'apple.008', 'window', 'door', 'apple.006', 'dish.001', 'jar.001', 'notebook.001', 'banana.004', 'spoon', 'bowl', 'banana.001', 'Pencil.003', 'mug.001', 'folder', 'notebook', 'paper.002', 'table.001', 'ball.001', 'wall.001', 'wall', 'shelf', 'Pencil.001', 'ball', 'goblet', 'lamp', 'jar', 'mug', 'bowl_001', 'Robot', 'chair', 'cup', 'Table', 'Floor']


def clean_name(obj):
    if '.' in obj.name:
        clean_name = obj.name[:obj.name.find(".")]
    elif '_' in obj.name:
        clean_name = obj.name[:obj.name.find("_")]
    else: 
        clean_name = obj.name
    return clean_name.lower()
    
def list_clean_names():
    names = []
    for obj in create_list_rigid_bodies():
        names.append(clean_name(obj))
    return names

def create_list_rigid_bodies():

    scene = bpy.data.scenes['Scene']

    bpy.context.screen.scene = scene
    
    rigid_body_list=[]
    for obj in scene.objects:
        if "highlight" not in obj.name:
            if obj.rigid_body is None:
                print("'"+obj.name+"'"+ " has not been included, to include it make sure it is a rigid body")
                pass
            else:
                rigid_body_list.append(obj)
    return rigid_body_list

def print_list_rigid_bodies():
    names = []
    for obj in create_list_rigid_bodies():
        names.append(obj.name)
    print(names)

def get_directory(dir):
    # This is the list of directories with the name and address
    directories={'bpy':'/bpy-scripts/',
                 'edits': '/bpy-scripts/scene editing/',
                 'bge':'/bge-scripts/',
                 'bgui':'/bgui-scripts/',
                 'blender':''}
    ## Blender is the default directory
    if dir is None:
        dir='blender'

    current_directory = os.getcwd()

    if os.path.basename(current_directory) == "blender":
        return current_directory + directories[dir]
    elif os.path.basename(os.path.dirname(current_directory)) == "blender":
        return os.path.dirname(current_directory) + directories[dir]
    else:
        print('ERROR: Terminal running blender should be running from the blender folder in the main project folder')

#### Link scripts to blender
def link_scripts(directory):
    ctx = bpy.context.copy()
    #Ensure  context area is not None
    ctx['area'] = ctx['screen'].areas[0]

    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            if filename in bpy.data.texts:
                pass

                    # # bpy.context.space_data.text = bpy.data.texts[filename] # These don't work when run from terminal
                    # # bpy.ops.text.reload()
            else:
                bpy.ops.text.open(filepath=directory + filename)
    #bpy.context.space_data.text = bpy.data.texts[0] # These don't work when run from terminal

def run_bpy_script(directory,scriptname):
    file = directory + scriptname 
    exec(compile(open(file).read(), file, 'exec'))

def run_edit_script(scriptname):
    file = get_directory('edits') + scriptname 
    exec(compile(open(file).read(), file, 'exec'))


#### Geometry Stuff

def get_bbox_centre(obj):
    local_bbox_center = 0.125 * sum((Vector(b) for b in obj.bound_box), Vector())
    global_bbox_center = obj.matrix_world * local_bbox_center
    return global_bbox_center
