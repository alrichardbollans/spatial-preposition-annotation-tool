### Adds logic to objects and cameras in blender scene

import bpy

import os

### blender_utils file should be in blender add ons directory. Usually .config/blender/2.79/scripts/addons
import blender_utils

print("The main scene containing various objects should be named 'Scene'")

class Task:
    main_scene = bpy.data.scenes["Scene"]
    def __init__(self,name,suffix):
        self.name = name # name of task
        self.suffix = suffix # abbreviation of task
    ####### CAMERA & Timer
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


    def add_general_logic(self,object_list):
        ### Link scripts
        bge_scripts_directory = blender_utils.get_directory('bge')

        bgui_scripts_directory = blender_utils.get_directory('bgui')

        blender_utils.link_scripts(bge_scripts_directory)

        blender_utils.link_scripts(bgui_scripts_directory)

        bpy_scripts_directory = blender_utils.get_directory('bpy')

        edits_scripts_directory = blender_utils.get_directory('edits')

        blender_utils.link_scripts(bpy_scripts_directory)

        blender_utils.link_scripts(edits_scripts_directory)

        ###### EMPTY
        
        ### Add empty object if there isn't one
        bpy.context.screen.scene =  self.main_scene 
        if "Empty" not in self.main_scene.objects:
            bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False, location=(0,0,0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            bpy.context.active_object.name = "Empty"
            print("Empty object was missing from main scene and has been added")
        ### Select empty object
        empty = self.main_scene.objects["Empty"]

        empty.select = True

        bpy.context.scene.objects.active = empty
        ### Clear empty game properties
        while len(empty.game.properties) != 0:
            bpy.ops.object.game_property_remove(index=0)

        ### Add game properties
        bpy.ops.object.game_property_new(type = "BOOL",name=self.name) # This should be added in the first position

        bpy.ops.object.game_property_new(type = "BOOL",name=self.suffix) #This allows the game to know which task we are doing.

        bpy.ops.object.game_property_new(type = "TIMER",name='game_time')

        bpy.ops.object.game_property_new(type = "BOOL",name=bpy.path.basename(bpy.context.blend_data.filepath))


        # Add general sensors
        bpy.ops.logic.sensor_add(type="ALWAYS",name="Always",object=empty.name)
        empty.game.sensors["Always"].use_pulse_true_level =True

        bpy.ops.logic.sensor_add(type="ALWAYS",name="AlwaysStartup",object=empty.name)
        # bpy.ops.logic.sensor_add(type="MESSAGE",name="start",object=obj.name)
        
        bpy.ops.logic.sensor_add(type="MESSAGE",name="deselect",object=empty.name)
        empty.game.sensors["deselect"].subject = "deselect"

        bpy.ops.logic.sensor_add(type="MESSAGE",name="change",object=empty.name)
        empty.game.sensors["change"].subject = "change"

        bpy.ops.logic.sensor_add(type="MESSAGE",name="changepreposition",object=empty.name)
        empty.game.sensors["changepreposition"].subject = "changepreposition"

        bpy.ops.logic.sensor_add(type="KEYBOARD",name="textinputkeyboard",object=empty.name)
        empty.game.sensors["textinputkeyboard"].use_all_keys = True

        bpy.ops.logic.sensor_add(type="MOUSE",name="leftClick",object=empty.name)
        empty.game.sensors["leftClick"].use_tap =True
        empty.game.sensors["leftClick"].mouse_event = "LEFTCLICK"

        bpy.ops.logic.sensor_add(type="MOUSE",name="rightClick",object=empty.name)
        empty.game.sensors["rightClick"].use_tap =True
        empty.game.sensors["rightClick"].mouse_event = "RIGHTCLICK"

        bpy.ops.logic.sensor_add(type="MOUSE",name="hoverAny",object=empty.name)
        empty.game.sensors["hoverAny"].mouse_event = "MOUSEOVERANY"

        
        bpy.ops.logic.controller_add(type="PYTHON",name="ObjectController",object=empty.name)

        empty.game.sensors["leftClick"].link(empty.game.controllers["ObjectController"])
        empty.game.sensors["rightClick"].link(empty.game.controllers["ObjectController"])
        empty.game.sensors["hoverAny"].link(empty.game.controllers["ObjectController"])
        empty.game.sensors["deselect"].link(empty.game.controllers["ObjectController"])

        empty.game.controllers["ObjectController"].text=bpy.data.texts["object_controller.py"]


        bpy.ops.logic.controller_add(type="PYTHON",name="startUp",object=empty.name)
        empty.game.controllers["startUp"].text=bpy.data.texts["on-startup.py"]
        empty.game.controllers["startUp"].use_priority =True
        empty.game.sensors["AlwaysStartup"].link(empty.game.controllers["startUp"])

        bpy.ops.logic.controller_add(type="PYTHON",name="textui",object=empty.name)
        empty.game.controllers["textui"].text=bpy.data.texts["textui_and_output.py"]
        empty.game.sensors["Always"].link(empty.game.controllers["textui"])
        empty.game.sensors["deselect"].link(empty.game.controllers["textui"])
        empty.game.sensors["textinputkeyboard"].link(empty.game.controllers["textui"])
        empty.game.sensors["changepreposition"].link(empty.game.controllers["textui"])

        bpy.ops.logic.actuator_add(type="GAME",name="END_GAME",object=empty.name)
        empty.game.actuators['END_GAME'].mode = 'QUIT'
        empty.game.actuators['END_GAME'].link(empty.game.controllers['textui'])

        ### OBJECTS

        for obj in object_list:
            bpy.ops.object.select_all(action='DESELECT')
            obj.select = True

            bpy.context.scene.objects.active = obj

            while len(obj.game.properties) != 0:
                bpy.ops.object.game_property_remove(index=0)
            if "used" not in obj.game.properties:

                bpy.ops.object.game_property_new(type = "BOOL",name="selectedfigure")

                bpy.ops.object.game_property_new(type = "BOOL", name="selectedground")

                bpy.ops.object.game_property_new(type = "BOOL",name="highlight")

                bpy.ops.object.game_property_new(type = "BOOL",name="used")


    def save_game_remove_logic(self):


        bpy.ops.wm.addon_enable(module="game_engine_save_as_runtime")
        bpy.context.screen.scene =  self.main_scene 
        bpy.ops.wm.save_as_runtime(filepath=blender_utils.get_directory('blender')+'/annotation scenes/'+bpy.path.basename(bpy.context.blend_data.filepath).replace(".blend","-"+self.suffix+".blend"))
        directory = blender_utils.get_directory('bpy')
        blender_utils.run_bpy_script(directory,"remove_all_logic.py")

class SemanticTask(Task):

    main_scene = bpy.data.scenes["Scene"]
    #preposition_overlay_scene = bpy.data.scenes["Scene.001"]

    def __init__(self,name,suffix,user_selections):
        Task.__init__(self,name,suffix)
        self.user_selections = user_selections #list of things user selects: "p","f", "g"


    ###### EMPTY
    def add_main_empty_logic(self):
        ### Deslect all objects
        bpy.ops.object.select_all(action='DESELECT')

        
        bpy.context.screen.scene =  self.main_scene 


        ### Select empty object
        empty = self.main_scene.objects["Empty"]

        empty.select = True

        bpy.context.scene.objects.active = empty

        bpy.ops.object.game_property_new(type = "BOOL",name='confirm')

        for x in self.user_selections:
            bpy.ops.object.game_property_new(type = "BOOL",name=x)

        ### Add sensors, controllers and links

        # bpy.ops.logic.controller_add(type="PYTHON",name="PythonOverlay",object=empty.name)
        # empty.game.controllers["PythonOverlay"].text=bpy.data.texts["open-overlay.py"]
        # empty.game.controllers["PythonOverlay"].use_priority =True
        # empty.game.sensors["AlwaysStartup"].link(empty.game.controllers["PythonOverlay"])

        

        # bpy.ops.logic.controller_add(type="PYTHON",name="outputs",object=empty.name)
        # empty.game.controllers["outputs"].text=bpy.data.texts["output_annotations.py"]
        # empty.game.sensors["Always"].link(empty.game.controllers["outputs"])
        # empty.game.sensors["deselect"].link(empty.game.controllers["outputs"])

        if self.suffix == "sp":
            bpy.ops.logic.controller_add(type="PYTHON",name="PythonHighlightFG",object=empty.name)
            empty.game.controllers["PythonHighlightFG"].text = bpy.data.texts["highlight_figure_ground.py"]
            for sens in empty.game.sensors:
                if sens.name in ["Always","change"]:
                    sens.link(empty.game.controllers["PythonHighlightFG"])

        if self.suffix == "sf":
            bpy.ops.logic.controller_add(type="PYTHON",name="PythonHighlightG",object=empty.name)
            empty.game.controllers["PythonHighlightG"].text = bpy.data.texts["highlight_ground.py"]
            for sens in empty.game.sensors:
                if sens.name in ["Always","change"]:
                    sens.link(empty.game.controllers["PythonHighlightG"])

        if self.suffix == "sg":
            bpy.ops.logic.controller_add(type="PYTHON",name="PythonHighlightF",object=empty.name)
            empty.game.controllers["PythonHighlightF"].text = bpy.data.texts["highlight_figure.py"]
            empty.game.actuators['END_GAME'].link(empty.game.controllers['PythonHighlightF'])
            for sens in empty.game.sensors:
                if sens.name in ["Always","change"]:
                    sens.link(empty.game.controllers["PythonHighlightF"])



    ####### OBJECTS
    def add_object_logic(self, object_list):
        bpy.context.screen.scene =  self.main_scene



        for obj in object_list:
            bpy.ops.object.select_all(action='DESELECT')
            obj.select = True

            bpy.context.scene.objects.active = obj


            if 'o' in self.user_selections or 'f' in self.user_selections or 'g' in self.user_selections:
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



    def add_logic(self):
        rigid_body_list = blender_utils.create_list_rigid_bodies()
        ### Start by clearing all logic from scene
        directory = blender_utils.get_directory('bpy')
        blender_utils.run_bpy_script(directory,"remove_all_logic.py")
        ### Start by deselecting all objects
        bpy.ops.object.select_all(action='DESELECT')



        self.add_general_logic(rigid_body_list)
        self.add_main_empty_logic()
        self.add_camera_navigation_logic()
        # self.add_object_logic(rigid_body_list)


class PragmaticTask(Task):

    main_scene = bpy.data.scenes["Scene"]
    #preposition_overlay_scene = bpy.data.scenes["Scene.001"]

    def __init__(self,name,suffix,instruction,highlighted_object):
        Task.__init__(self,name,suffix)
        self.instruction = instruction
        self.highlighted_object = highlighted_object

    ###### EMPTY
    def add_main_empty_logic(self):
        ### Deslect all objects
        bpy.ops.object.select_all(action='DESELECT')

        
        bpy.context.screen.scene =  self.main_scene 


        ### Select empty object
        empty = self.main_scene.objects["Empty"]

        empty.select = True

        bpy.context.scene.objects.active = empty

        bpy.ops.object.game_property_new(type = "BOOL",name='pragmatic')

        bpy.ops.object.game_property_new(type = "BOOL",name=self.highlighted_object)

        ### Add sensors, controllers and links

        
   
        
        if self.suffix == "p1":
            bpy.ops.logic.controller_add(type="PYTHON",name="PythonHighlightF",object=empty.name)
            empty.game.controllers["PythonHighlightF"].text = bpy.data.texts["highlight_figure.py"]
            empty.game.actuators['END_GAME'].link(empty.game.controllers['PythonHighlightF'])
            for sens in empty.game.sensors:
                if sens.name in ["Always","change"]:
                    sens.link(empty.game.controllers["PythonHighlightF"])



    ####### OBJECTS
    def add_object_logic(self, object_list):
        bpy.context.screen.scene =  self.main_scene



    def add_logic(self):
        rigid_body_list = blender_utils.create_list_rigid_bodies()
        ### Start by clearing all logic from scene
        directory = blender_utils.get_directory('bpy')
        blender_utils.run_bpy_script(directory,"remove_all_logic.py")
        ### Start by deselecting all objects
        bpy.ops.object.select_all(action='DESELECT')



        self.add_general_logic(rigid_body_list)
        self.add_main_empty_logic()
        self.add_camera_navigation_logic()
        self.add_object_logic(rigid_body_list)











def prepare_scene():
    bpy_scripts_directory = blender_utils.get_directory('bpy')

    edits_scripts_directory = blender_utils.get_directory('edits')
    
    blender_utils.link_scripts(bpy_scripts_directory)

    blender_utils.link_scripts(edits_scripts_directory)

    #blender_utils.run_bpy_script(directory,"edit_physics.py")
    blender_utils.run_bpy_script(bpy_scripts_directory,"edit_rendering_and_settings.py")
    blender_utils.run_bpy_script(bpy_scripts_directory,"create_highlights.py")
    blender_utils.run_bpy_script(bpy_scripts_directory,"remove_all_logic.py")

prepare_scene()

list_of_tasks = []

standard = SemanticTask('Standard Task','s',["p","f", "g"])
# list_of_tasks.append(standard)

selectprep = SemanticTask('Choose Preposition','sp',['p'])
# list_of_tasks.append(selectprep)

selectfg = SemanticTask('Select Figure & Ground','sfg',["f","g"])
list_of_tasks.append(selectfg)

selectg = SemanticTask('Select Ground','sg',["g"])
# list_of_tasks.append(selectg)

selectf = SemanticTask('Select Figure','sf',["f"])
# list_of_tasks.append(selectf)

pass_object = PragmaticTask('Identification Task','p1','Provide the robot with a description of the location of the highlighted object','f')
list_of_tasks.append(pass_object)

main_scene = bpy.data.scenes["Scene"]

for task in list_of_tasks:
    task.add_logic()
    task.save_game_remove_logic()

