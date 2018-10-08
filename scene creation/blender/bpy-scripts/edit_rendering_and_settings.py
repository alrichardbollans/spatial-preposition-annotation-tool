import bpy

### Object Settings
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
			if obj.active_material.texture_slots[0] is None:
				pass
			else:
				obj.active_material.texture_slots[0].texture_coords = 'GLOBAL'

main_scene = bpy.data.scenes["Scene"]
bpy.context.screen.scene =  main_scene 

mat = add_material_to_scene(main_scene)
add_material_to_objects(main_scene,mat)


### World Settings
bpy.data.worlds["World"].horizon_color = (0.487, 0.404, 0.208)

main_scene.world.light_settings.use_environment_light = True

main_scene.world.light_settings.environment_energy = 0.1

### Game Settings

main_scene.game_settings.material_mode = 'GLSL' #For proper texture and shading

main_scene.game_settings.show_mouse = True #So that mouse is visible in game

main_scene.game_settings.physics_engine = 'BULLET' # Needed for hitboxes used by mouseover sensor

for mat in bpy.data.materials:
	mat.game_settings.use_backface_culling = False



### Menu Settings
#def hide_menu_render(name):
#	bpy.data.scenes["Scene"].objects[name].hide_render = True

# hide_menu_render('exit')
# hide_menu_render('cancel')
# hide_menu_render('background')


