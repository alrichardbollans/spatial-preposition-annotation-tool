### to run once on all scenes
### Creates red/blue wireframes of objects set in another layer ot highlight figure/ground
### Note this uses RED and BLUE wireframe to highlight objects => don't use red as a color for objects
### idea is to create a copy of object
# with separate material 
# remove texture 
# set diffuse color and wire render
# remove object color  and use_mist from opitons
import bpy
import random




###### Create list of tangible objects
def create_list_rigid_bodies(scene):
	rigid_body_list=[]
	for obj in scene.objects:
		if "highlight" not in obj.name:
			if obj.rigid_body is None:
				pass
				#print("'"+obj.name+"'"+ " has not been included, to include it make sure it is a rigid body")
			else:
				rigid_body_list.append(obj)
	#print("rigid body list ="+str(rigid_body_list))
	return rigid_body_list

def remove_all_highlights():
	# first remove all highlights
	bpy.ops.object.select_all(action='DESELECT')
	for obj in bpy.data.objects:
		if 'highlight' in obj.name:
			obj.select = True
	bpy.context.scene.layers[1] = True
	bpy.ops.object.delete()
	bpy.context.scene.layers[1] = False

####### Create duplicate objects to highlight figure

def create_highlight_duplicates(scene,object_list,use):


	#select the object and make it active
	for obj in object_list:
		
		if 'highlight' not in obj.name:

			bpy.ops.object.select_all(action='DESELECT')

			### Create a duplicate
			obj.select = True

			bpy.context.scene.objects.active = obj

			bpy.context.screen.scene =  scene 

			bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False}) #This is giving a context error but I don't think it matters

			### Unlink the material and texture
			bpy.ops.object.make_single_user(object=False,obdata=False,material=True,texture=True,animation=False)
			## Edit ALL materials of duplicate


			#material = bpy.context.active_object.active_material
			for m in bpy.context.active_object.material_slots:
				m.material.type = "WIRE" #If this gives an error, check if any of the objects have blank m.material slots

				m.material.use_object_color = False

				m.material.use_mist = False
				if use =="f":
					m.material.diffuse_color = [0,0.8,0]
				if use =="g":
					m.material.diffuse_color = [0.8,0,0]

				# m.material.use_tangent_shading = True

				m.material.use_shadeless = True

				# Remove texture
				m.material.use_textures[0] = False

			#
			#bpy.ops.transform.resize((1.1,1.1,1.1))

			# Add highlight property
			bpy.ops.object.game_property_new(type = "BOOL",name="highlight")

			# bpy.context.active_object['highlight'] = True#.game.properties[2] = True#['highlight']

			# Hide object in another layer
			bpy.ops.object.move_to_layer(layers=(False,True,False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

			# Make no longer rigid body
			bpy.ops.rigidbody.object_remove()
			
			# Rename
			bpy.context.active_object.name = obj.name + "highlight" + use
			# print(bpy.context.active_object.name)
			#Deselect
			obj.select = False


			

main_scene = bpy.data.scenes["Scene"]

bpy.context.screen.scene =  main_scene



rigid_bodies = create_list_rigid_bodies(main_scene)

remove_all_highlights()
create_highlight_duplicates(main_scene,rigid_bodies,"f")
create_highlight_duplicates(main_scene,rigid_bodies,"g")









# ####### Create duplicate objects to highlight ground

# for obj in rigid_objects:
# # fig = random.choice(rigid_objects) # randomly pick an object
# # print("figure ="+ fig)

#  #select the object and make it active

# 	obj.select = True

# 	bpy.context.scene.objects.active = obj

# 	### Create a duplicate
# 	bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False})

# 	### Unlink the material and texture
# 	bpy.ops.object.make_single_user(object=False,obdata=False,material=True,texture=True,animation=False)

# 	## Edit material of duplicate

# 	material = bpy.context.active_object.active_material

# 	material.type = "WIRE"

# 	material.use_object_color = False

# 	material.use_mist = False

# 	material.diffuse_color = [0,0,0.8]

# 	# material.use_tangent_shading = True

# 	material.use_shadeless = True



# 	# Remove texture

# 	material.use_textures[0] = False

# 	# Add highlight property anmd set to true

# 	bpy.ops.object.game_property_new(type = "BOOL",name="highlight")

# 	# bpy.context.active_object['highlight'] = True

# 	# Hide object in another layer	

# 	bpy.ops.object.move_to_layer(layers=(False,True,False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	
# 	# Make no longer rigid body

# 	bpy.ops.rigidbody.object_remove()
# 	bpy.context.active_object.name = obj.name + "highlightg"
# 	obj.select = False


# for obj in scene.objects:
# 	if obj.layers[1]:
# 		obj['highlight'] =True

# ### Highlight ground

# ground = random.choice(rigid_objects) # randomly pick an object
# print("ground ="+ground)

#  #select the object and make it active

# ground.select = True

# bpy.context.scene.objects.active = ground

# ### Create a duplicate
# bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False})

# ### Unlink the material and texture
# bpy.ops.object.make_single_user(object=False,obdata=False,material=True,texture=True,animation=False)

# ## Edit material of duplicate

# material = bpy.context.active_object.active_material

# material.type = "WIRE"

# material.use_object_color = False

# material.use_mist = False

# material.diffuse_color = [0,0,0.8]

# material.use_tangent_shading = True

# material.use_shadeless = True

# # Remove texture

# material.use_textures[0] = False
