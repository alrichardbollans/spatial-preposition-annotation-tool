import bpy


def add_material_to_scene(scene):

	mat = bpy.data.materials.get("Material")
	if mat is None:
	    # create material
	    mat = bpy.data.materials.new(name="Material")
	return mat

def add_material_to_objects(scene,mat): #this is needed so colors change on click
	for obj in scene.objects: 
		if hasattr(obj.data,"materials"):			
			if len(obj.data.materials)==0:
				obj.data.materials.append(mat)
		if obj.active_material is None:
			pass
		else:
			obj.active_material.use_object_color = True

main_scene = bpy.data.scenes["Scene"]
bpy.context.screen.scene =  main_scene 

mat = add_material_to_scene(main_scene)
add_material_to_objects(main_scene,mat)