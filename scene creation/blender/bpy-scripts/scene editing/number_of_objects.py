import bpy

import blender_utils

main_scene = bpy.context.scene

list_objs = []

for obj in main_scene.objects:
	if obj.rigid_body is None:
		pass
	elif 'highlight' not in obj.name:
		list_objs.append(obj)

print("Number of Objects: "+ str(len(list_objs)))

def list_clean_names():
    names = []
    for obj in list_objs:
        names.append(blender_utils.clean_name(obj))
    return names

figure_list = []
non_figure_list = ['wall','ceiling','floor']
for obj in list_objs:
	if list_clean_names().count(blender_utils.clean_name(obj))>1 and blender_utils.clean_name(obj) not in non_figure_list:
		figure_list.append(obj.name)

print('Number of possible figures for pragmatic task: ' +str(len(figure_list)))
print(figure_list)