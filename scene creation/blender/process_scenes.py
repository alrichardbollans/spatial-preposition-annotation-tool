
#### Runs link_scripts on all scene files, which finalizes evertything

import os

import inspect

scene_directory = "scenes/"

def create_games(scene_directory):
	for filename in os.listdir(scene_directory):
		if filename.endswith(".blend"):
			os.system("blender scenes/" + filename + " --background --python bpy-scripts/add_logics_properties_save_game.py")

create_games(scene_directory)

# def run_link_scripts(scene_directory):
# 	for filename in os.listdir(scene_directory):
# 		if filename.endswith(".blend"):
# 			#os.system("blender scenes/" + filename + " --background --python bpy-scripts/extract_properties.py")
# 			os.system("blender scenes/" + filename + " --background --python bpy-scripts/edit_physics.py")
# 			os.system("blender scenes/" + filename + " --background --python bpy-scripts/edit_rendering.py")
# 			os.system("blender scenes/" + filename + " --background --python bpy-scripts/highlighting/create_highlights.py")
# 			os.system("blender scenes/" + filename + " --background --python bpy-scripts/remove_all_logic.py")


# run_link_scripts(scene_directory)

#### adds logic and saves game engine





			# os.system("blender scenes/" + filename + " --background --python bpy-scripts/add_logic.py -- --task="+task)
			# #os.system("blender scenes/" + filename + " --background --python bpy-scripts/save-game-engine.py -- --task="+task)

			# os.system("blender scenes/" + filename + " --background --python bpy-scripts/remove_all_logic.py")



# task_list = ["s","hfg"]
#for x in task_list:
    #create_games(x,scene_directory)

# bpy.ops.script.python_file_run(filepath="blender/bpy-scripts/add_logic.py")
# bpy.ops.wm.save_as_runtime(filepath=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))))+'/annotation-scenes/'+bpy.path.basename(bpy.context.blend_data.filepath))
# bpy.ops.script.python_file_run(filepath="blender/bpy-scripts/remove_all_logic.py")

 