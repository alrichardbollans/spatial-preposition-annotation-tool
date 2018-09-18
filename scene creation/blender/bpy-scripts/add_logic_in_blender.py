### Adds logic to objects and cameras in blender scene

import bpy

import os


print("The main scene containing various objects should be named 'Scene', the overlay scene containing the prepositionn menu should be called 'Scene.001'")

class SemanticTask:
    suffix = '' #string. abbreviation of task
    user_selections = [] #list of things user selects: "p","o","f", "g"
    highlighted_objects = [] #list of types of objects that may need highlighting
    main_scene = bpy.data.scenes["Scene"]
    preposition_overlay_scene = bpy.data.scenes["Scene.001"]

    ###### EMPTY
    def add_main_empty_logic(self):
        bpy.ops.object.select_all(action='DESELECT')

        bpy.context.screen.scene =  self.main_scene 
        if "Empty" not in self.main_scene.objects:
            bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False, location=(0,0,0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            bpy.context.active_object.name = "Empty"
            print("Empty object was missing from main scene and has been added")

        empty = self.main_scene.objects["Empty"]

        empty.select = True

        bpy.context.scene.objects.active = empty


        bpy.ops.logic.sensor_add(type="ALWAYS",name="Always",object=empty.name)
        empty.game.sensors["Always"].use_pulse_true_level =True
        bpy.ops.logic.sensor_add(type="ALWAYS",name="AlwaysStartup",object=empty.name)
        # bpy.ops.logic.sensor_add(type="MESSAGE",name="start",object=obj.name)
        
        bpy.ops.logic.sensor_add(type="MESSAGE",name="deselect",object=empty.name)
        empty.game.sensors["deselect"].subject = "deselect"

        bpy.ops.logic.sensor_add(type="MESSAGE",name="change",object=empty.name)
        
        bpy.ops.logic.controller_add(type="PYTHON",name="PythonOverlay",object=empty.name)
        empty.game.controllers["PythonOverlay"].text=bpy.data.texts["open-overlay.py"]
        empty.game.controllers["PythonOverlay"].use_priority =True
        empty.game.sensors["AlwaysStartup"].link(empty.game.controllers["PythonOverlay"])

        bpy.ops.logic.controller_add(type="PYTHON",name="startUp",object=empty.name)
        empty.game.controllers["startUp"].text=bpy.data.texts["on-startup.py"]
        empty.game.controllers["startUp"].use_priority =True
        empty.game.sensors["AlwaysStartup"].link(empty.game.controllers["startUp"])
                
        bpy.ops.logic.controller_add(type="PYTHON",name="outputs",object=empty.name)
        empty.game.controllers["outputs"].text=bpy.data.texts["output_annotations.py"]
        empty.game.sensors["Always"].link(empty.game.controllers["outputs"])
        empty.game.sensors["deselect"].link(empty.game.controllers["outputs"])

        if self.suffix == "sp":
            bpy.ops.logic.controller_add(type="PYTHON",name="PythonHighlightFG",object=empty.name)
            empty.game.controllers["PythonHighlightFG"].text = bpy.data.texts["highlight_figure_ground.py"]
            for sens in empty.game.sensors:
                if sens.name in ["Always","change"]:
                    sens.link(empty.game.controllers["PythonHighlightFG"])
    ####### CAMERA
    def add_camera_navigation_logic(self):
        bpy.context.screen.scene =  self.main_scene 
        if "Camera" not in self.main_scene.objects:

            bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(6.53031, -4.49495, 4.71519), rotation=(1.24226, -2.446e-07, 1.27125), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            bpy.context.active_object.name = "Camera"
            print("Camera object was missing from main scene and has been added")

        camera = self.main_scene.objects["Camera"]
        ## SENSORS
        bpy.ops.logic.sensor_add(type="MOUSE",name="mouseMove",object=camera.name)
        camera.game.sensors["mouseMove"].mouse_event = "MOVEMENT"

        bpy.ops.logic.sensor_add(type="KEYBOARD",name="keyUp",object=camera.name)
        camera.game.sensors["keyUp"].key = "UP_ARROW"

        bpy.ops.logic.sensor_add(type="KEYBOARD",name="keyDown",object=camera.name)
        camera.game.sensors["keyDown"].key = "DOWN_ARROW"

        bpy.ops.logic.sensor_add(type="KEYBOARD",name="keyLeft",object=camera.name)
        camera.game.sensors["keyLeft"].key = "LEFT_ARROW"


        bpy.ops.logic.sensor_add(type="KEYBOARD",name="keyRight",object=camera.name)
        camera.game.sensors["keyRight"].key = "RIGHT_ARROW"

        bpy.ops.logic.sensor_add(type="MOUSE",name="wheelUp",object=camera.name)
        camera.game.sensors["wheelUp"].mouse_event = "WHEELUP"

        bpy.ops.logic.sensor_add(type="MOUSE",name="wheelDown",object=camera.name)
        camera.game.sensors["wheelDown"].mouse_event = "WHEELDOWN"

        ## CONTROLLERS
        bpy.ops.logic.controller_add(type="LOGIC_AND",name="and0",object=camera.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND",name="and1",object=camera.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND",name="and2",object=camera.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND",name="and3",object=camera.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND",name="and4",object=camera.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND",name="and5",object=camera.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND",name="and6",object=camera.name)

        ## ACTUATORS
        bpy.ops.logic.actuator_add(type="MOUSE",name="mouseLook",object=camera.name)
        camera.game.actuators["mouseLook"].mode = "LOOK"
        camera.game.actuators["mouseLook"].use_axis_x = True
        camera.game.actuators["mouseLook"].use_axis_y = True
        camera.game.actuators["mouseLook"].sensitivity_x = 2
        camera.game.actuators["mouseLook"].sensitivity_y = 2
        camera.game.actuators["mouseLook"].min_x = 0
        camera.game.actuators["mouseLook"].max_x = 0
        camera.game.actuators["mouseLook"].min_y = -1.570796
        camera.game.actuators["mouseLook"].max_y = 1.570796
        camera.game.actuators["mouseLook"].object_axis_x = "OBJECT_AXIS_Z"
        camera.game.actuators["mouseLook"].object_axis_y = "OBJECT_AXIS_X"
        camera.game.actuators["mouseLook"].local_x = False

        bpy.ops.logic.actuator_add(type="MOTION",name="forward",object=camera.name)
        camera.game.actuators["forward"].mode = "OBJECT_NORMAL"
        camera.game.actuators["forward"].offset_location[2] = -0.1

        bpy.ops.logic.actuator_add(type="MOTION",name="backward",object=camera.name)
        camera.game.actuators["backward"].mode = "OBJECT_NORMAL"
        camera.game.actuators["backward"].offset_location[2] = 0.1

        bpy.ops.logic.actuator_add(type="MOTION",name="left",object=camera.name)
        camera.game.actuators["left"].mode = "OBJECT_NORMAL"
        camera.game.actuators["left"].offset_location[0] = -0.1

        bpy.ops.logic.actuator_add(type="MOTION",name="right",object=camera.name)
        camera.game.actuators["right"].mode = "OBJECT_NORMAL"
        camera.game.actuators["right"].offset_location[0] = 0.1

        ## Connections
        camera.game.sensors["mouseMove"].link(camera.game.controllers["and0"])
        camera.game.sensors["keyUp"].link(camera.game.controllers["and1"])
        camera.game.sensors["keyDown"].link(camera.game.controllers["and2"])
        camera.game.sensors["keyLeft"].link(camera.game.controllers["and3"])
        camera.game.sensors["keyRight"].link(camera.game.controllers["and4"])
        camera.game.sensors["wheelUp"].link(camera.game.controllers["and5"])
        camera.game.sensors["wheelDown"].link(camera.game.controllers["and6"])

        camera.game.actuators["mouseLook"].link(camera.game.controllers["and0"])
        camera.game.actuators["forward"].link(camera.game.controllers["and1"])
        camera.game.actuators["backward"].link(camera.game.controllers["and2"])
        camera.game.actuators["left"].link(camera.game.controllers["and3"])
        camera.game.actuators["right"].link(camera.game.controllers["and4"])
        camera.game.actuators["forward"].link(camera.game.controllers["and5"])
        camera.game.actuators["backward"].link(camera.game.controllers["and6"])

        ##########

    ####### OBJECTS
    def add_object_logic(self, object_list):
        bpy.context.screen.scene =  self.main_scene


        for obj in object_list:
            bpy.ops.object.select_all(action='DESELECT')
            obj.select = True

            bpy.context.scene.objects.active = obj
            if "selectedfigure" not in obj.game.properties:

                bpy.ops.object.game_property_new(type = "BOOL",name="selectedfigure")

                bpy.ops.object.game_property_new(type = "BOOL", name="selectedground")

                bpy.ops.object.game_property_new(type = "BOOL",name="highlight")

            bpy.ops.logic.sensor_add(type="MOUSE",name="leftClick",object=obj.name)
            obj.game.sensors["leftClick"].use_tap =True
            obj.game.sensors["leftClick"].mouse_event = "LEFTCLICK"

            bpy.ops.logic.sensor_add(type="MOUSE",name="rightClick",object=obj.name)
            obj.game.sensors["rightClick"].use_tap =True
            obj.game.sensors["rightClick"].mouse_event = "RIGHTCLICK"

            bpy.ops.logic.sensor_add(type="MOUSE",name="MouseOver",object=obj.name)
            obj.game.sensors["MouseOver"].mouse_event = "MOUSEOVER"

            bpy.ops.logic.sensor_add(type="MESSAGE",name="deselect",object=obj.name)
            obj.game.sensors["deselect"].subject = "deselect"

            bpy.ops.logic.controller_add(type="PYTHON",name="PythonMouse",object=obj.name)

            obj.game.sensors["leftClick"].link(obj.game.controllers["PythonMouse"])
            obj.game.sensors["rightClick"].link(obj.game.controllers["PythonMouse"])
            obj.game.sensors["MouseOver"].link(obj.game.controllers["PythonMouse"])
            obj.game.sensors["deselect"].link(obj.game.controllers["PythonMouse"])

            obj.game.controllers["PythonMouse"].text=bpy.data.texts["object-controller-"+self.suffix+".py"]

            

            obj.select = False

    ##### Preposition Overlay

    def add_overlay_empty_logic(self):
        if self.suffix =='sfg':

            bpy.ops.object.select_all(action='DESELECT')

            bpy.context.screen.scene =  self.preposition_overlay_scene 
            if "Empty.001" not in self.preposition_overlay_scene.objects:
                bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False, location=(0,0,0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
                bpy.context.active_object.name = "Empty.001"
                print("Empty object was missing from main scene and has been added")

            empty = self.preposition_overlay_scene.objects["Empty.001"]

            empty.select = True

            bpy.context.scene.objects.active = empty

            bpy.ops.logic.sensor_add(type="ALWAYS",name="Always",object=empty.name)
            empty.game.sensors["Always"].use_pulse_true_level =True


            bpy.ops.logic.sensor_add(type="MESSAGE",name="changepreposition",object=empty.name)

            bpy.ops.logic.controller_add(type="PYTHON",name="highlight",object=empty.name)
            empty.game.controllers["highlight"].text=bpy.data.texts["highlight_preposition.py"]

            
            empty.game.sensors["Always"].link(empty.game.controllers["highlight"])
            empty.game.sensors["changepreposition"].link(empty.game.controllers["highlight"])



    def add_preposition_property(self):
        if self.suffix =='sfg':
            bpy.context.screen.scene =  self.preposition_overlay_scene 
            for obj in self.preposition_overlay_scene.objects:

                if "preposition" in obj.game.properties:

                    obj.select = True

                    bpy.context.scene.objects.active = obj

                    bpy.ops.object.game_property_new(type = "BOOL",name="selectedprep")
                    
                    obj.select =False

    def add_preposition_selection_camera_logic(self):
        bpy.context.screen.scene =  self.preposition_overlay_scene
        if "Camera.001" not in self.preposition_overlay_scene.objects:
            bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0,0,11), rotation=(0,0,0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            bpy.context.active_object.name = "Camera.001"
            print("Camera object was missing from preposition overlay scene and has been added")
        
        text_camera = self.preposition_overlay_scene.objects["Camera.001"]

        bpy.ops.logic.sensor_add(type="MOUSE",name="mouseMove",object=text_camera.name)
        text_camera.game.sensors["mouseMove"].mouse_event = "MOVEMENT"

        bpy.ops.logic.controller_add(type="LOGIC_AND",name="and0",object=text_camera.name)

        bpy.ops.logic.actuator_add(type="MOUSE",name="mouseLook",object=text_camera.name)
        text_camera.game.actuators["mouseLook"].mode = "LOOK"
        text_camera.game.actuators["mouseLook"].use_axis_x = True
        text_camera.game.actuators["mouseLook"].use_axis_y = True
        text_camera.game.actuators["mouseLook"].sensitivity_x = 2
        text_camera.game.actuators["mouseLook"].sensitivity_y = 2
        text_camera.game.actuators["mouseLook"].min_x = 0
        text_camera.game.actuators["mouseLook"].max_x = 0
        text_camera.game.actuators["mouseLook"].min_y = -1.570796
        text_camera.game.actuators["mouseLook"].max_y = 1.570796
        text_camera.game.actuators["mouseLook"].object_axis_x = "OBJECT_AXIS_Y"
        text_camera.game.actuators["mouseLook"].object_axis_y = "OBJECT_AXIS_X"
        text_camera.game.actuators["mouseLook"].local_x = False

        text_camera.game.sensors["mouseMove"].link(text_camera.game.controllers["and0"])
        text_camera.game.actuators["mouseLook"].link(text_camera.game.controllers["and0"])

    def add_preposition_menu_logic(self):
        bpy.context.screen.scene =  self.preposition_overlay_scene 

        for obj in self.preposition_overlay_scene.objects:
            if obj.name == "cancel" or obj.name == "exit":
                bpy.ops.logic.sensor_add(type="MOUSE",name="leftClick",object=obj.name)
                obj.game.sensors["leftClick"].use_tap =True
                obj.game.sensors["leftClick"].mouse_event = "LEFTCLICK"

                bpy.ops.logic.sensor_add(type="MOUSE",name="MouseOver",object=obj.name)
                obj.game.sensors["MouseOver"].mouse_event = "MOUSEOVER"

                bpy.ops.logic.controller_add(type="PYTHON",name="PythonMouse",object=obj.name)
                obj.game.controllers["PythonMouse"].text=bpy.data.texts[obj.name+"-button.py"]

                obj.game.sensors["leftClick"].link(obj.game.controllers["PythonMouse"])
                obj.game.sensors["MouseOver"].link(obj.game.controllers["PythonMouse"])

        if "p" in self.user_selections:
            for obj in self.preposition_overlay_scene.objects:

                if "preposition" in obj.game.properties:

                    obj.select = True

                    bpy.context.scene.objects.active = obj

                    bpy.ops.object.game_property_new(type = "BOOL",name="selectedprep")

                    bpy.ops.logic.sensor_add(type="MOUSE",name="leftClick",object=obj.name)
                    obj.game.sensors["leftClick"].use_tap =True
                    obj.game.sensors["leftClick"].mouse_event = "LEFTCLICK"

                    bpy.ops.logic.sensor_add(type="MOUSE",name="MouseOver",object=obj.name)
                    obj.game.sensors["MouseOver"].mouse_event = "MOUSEOVER"

                    bpy.ops.logic.sensor_add(type="MESSAGE",name="deselect",object=obj.name)
                    obj.game.sensors["deselect"].subject = "deselect"

                    bpy.ops.logic.controller_add(type="PYTHON",name="PythonMouse",object=obj.name)
                    obj.game.controllers["PythonMouse"].text=bpy.data.texts["menu-controller-"+self.suffix+".py"]

                    obj.game.sensors["leftClick"].link(obj.game.controllers["PythonMouse"])
                    obj.game.sensors["MouseOver"].link(obj.game.controllers["PythonMouse"])
                    obj.game.sensors["deselect"].link(obj.game.controllers["PythonMouse"])
                obj.select =False






    def add_logic(self):
        ### Start by clearing all logic from scene
        directory = get_directory('bpy')
        run_bpy_script(directory,"remove_all_logic.py")
        ### Start by deselecting all objects
        bpy.ops.object.select_all(action='DESELECT')

        rigid_body_list = create_list_rigid_bodies(self.main_scene)

        bge_scripts_directory = get_directory('bge')

        link_scripts(bge_scripts_directory)

        self.add_main_empty_logic()
        self.add_camera_navigation_logic()
        self.add_object_logic(rigid_body_list)


        self.add_preposition_property()
        self.add_overlay_empty_logic()
        self.add_preposition_selection_camera_logic()
        self.add_preposition_menu_logic()

        #bpy.ops.wm.save_mainfile()
    def save_game_remove_logic(self):


        bpy.ops.wm.addon_enable(module="game_engine_save_as_runtime")
        bpy.context.screen.scene =  self.main_scene 
        bpy.ops.wm.save_as_runtime(filepath=get_directory()+'/annotation scenes/'+bpy.path.basename(bpy.context.blend_data.filepath).replace(".blend","-"+self.suffix+".blend"))
        directory = get_directory('bpy')
        run_bpy_script(directory,"remove_all_logic.py")



#### Link scripts to blender
def link_scripts(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            
            bpy.ops.text.open(filepath=directory + filename)


### For all rigid objects add the appropriate logic bricks and properties
def create_list_rigid_bodies(scene):
    bpy.context.screen.scene =  scene 
    rigid_body_list=[]
    for obj in scene.objects:
        if obj.rigid_body is None:
            print("'"+obj.name+"'"+ " has not been included, to include it make sure it is a rigid body")
        else:
            rigid_body_list.append(obj)
    return rigid_body_list

def get_directory(dir):
    # This is the list of directories with the name and address
    directories={'bpy':'/bpy-scripts/',
                 'bge':'/bge-scripts/',
                 'blender':''}
    ## Blender is the default directory
    if dir is None:
        dir='blender'

    current_directory = os.getcwd()
    if os.path.basename(current_directory) == "blender":
        return current_directory + directories[dir]
    if os.path.basename(os.path.dirname(current_directory)) == "blender":
        return os.path.dirname(current_directory) + directories[dir]


def run_bpy_script(directory,scriptname):
    file = directory + scriptname 
    exec(compile(open(file).read(), file, 'exec'))

def prepare_scene():
    directory = get_directory('bpy')

    link_scripts(directory)

    run_bpy_script(directory,"edit_physics.py")
    run_bpy_script(directory,"edit_rendering.py")
    run_bpy_script(directory,"create_highlights.py")
    run_bpy_script(directory,"remove_all_logic.py")

prepare_scene()

selectfg = SemanticTask()
selectfg.suffix = "sfg"
selectfg.user_selections = ["o","f", "g"]

selectfg.add_logic()

# list_of_tasks = []
# standard = SemanticTask()
# standard.suffix = "s"
# standard.user_selections = ["p","o","f", "g"]

# list_of_tasks.append(standard)

# selectprep = SemanticTask()
# selectprep.suffix = "sp"
# selectprep.user_selections = ["p"]

# list_of_tasks.append(selectprep)



# list_of_tasks.append(selectfg)

# for task in list_of_tasks:
#     task.add_logic()
#     task.save_game_remove_logic()

# def get_bpy_script_directory():
#     current_directory = os.getcwd()
#     if os.path.basename(current_directory) == "blender":
#         return current_directory+"/bpy-scripts/"
#     if os.path.basename(os.path.dirname(current_directory)) == "blender":
#         return os.path.dirname(current_directory)+"/bpy-scripts/"
# def get_bge_script_directory():

#     current_directory = os.getcwd()
#     if os.path.basename(current_directory) == "blender":
#         return current_directory+"/bge-scripts/"
#     if os.path.basename(os.path.dirname(current_directory)) == "blender":
#         return os.path.dirname(current_directory)+"/bge-scripts/"
# def get_blender_directory():
#     current_directory = os.getcwd()
#     if os.path.basename(current_directory) == "blender":
#         return current_directory
#     if os.path.basename(os.path.dirname(current_directory)) == "blender":
#         return os.path.dirname(current_directory)