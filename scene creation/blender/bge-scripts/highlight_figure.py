### Script that runs continuously with an always sensor in an Empty object
### Note this uses RED and BLUE wireframe to highlight objects => don't use red as a color for objects
### idea is to create a copy of object
# with separate material 
# remove texture 
# set diffuse color and wire render
# remove object color  and use mistfrom opitons
import bge
import random


scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
own = cont.owner #owner of the controller is the active object

scenes = bge.logic.getSceneList()

main_scene = scene

change = cont.sensors["change"]

end_game = cont.actuators['END_GAME']

def quit_game():
    cont.activate(end_game)

def clean_name(obj):
    if '.' in obj.name:
        clean_name = obj.name[:obj.name.find(".")]
    elif '_' in obj.name:
        clean_name = obj.name[:obj.name.find("_")]
    else: 
        clean_name = obj.name
    return clean_name.lower()
    
def list_clean_names(object_list):
    names = []
    for obj in object_list:
        names.append(clean_name(obj))
    return names

if change.positive:

	for obj in main_scene.objects:
		if obj.get('highlight')==True:
			obj.endObject()

		if obj.get('selectedfigure') == True:

			# obj.color-=x
			obj['selectedfigure']=False
	### Make list of rigid bodies
	rigid_objects=[]
	for obj in main_scene.objects:
		if "selectedfigure" in obj.getPropertyNames() and 'highlight' not in obj.name:
			rigid_objects.append(obj)
	#Make list of rigid bodies of which there are at least two
	figure_list = []
	non_figure_list = ['wall','ceiling','floor']
	for obj in rigid_objects:
		if list_clean_names(rigid_objects).count(clean_name(obj))>1 and obj['used'] ==False and clean_name(obj) not in non_figure_list:
			figure_list.append(obj)
		
	if len(figure_list) == 0:
		quit_game()
	else:
		fig = random.choice(figure_list) # randomly pick an object
		print("figure = "+ str(fig))
		highlighter_object = scene.addObject(fig.name+"highlightf")

		fig['selectedfigure']= True
		fig['used'] =True
















# highlighter_object.worldPosition = test.worldPosition
# highlighter_object.localPosition = test.localPosition
# highlighter_object.worldScale = test.worldScale
# highlighter_object.worldOrientation = test.worldOrientation

# # print(highlighter_object.meshes)
# # print(test.meshes)

# highlighter_object.replaceMesh(test.meshes[0], True)
# highlighter_object.meshes[0].materials[0]=material_i_want
# for material in highlighter_object.meshes[0].materials:
# 	material.diffuse = [0.8,0,0]
# 	material.activate()

# highlighter_object.meshes[0].materials[0] = highlight_material




# ####### Highlight figure object
# if start.positive:
# 	###### Create list of tangible objects
# 	rigid_objects=[]
# 	for obj in scene.objects:
# 		#print(obj)
# 		if obj.name != "Camera" and obj.name != "Lamp" and obj.name != "Empty"  and obj.name != "__default__cam__":
# 			rigid_objects.append(obj)

# 	fig = random.choice(rigid_objects) # randomly pick an object
# 	print("figure = "+ str(fig))

# 	fig.color += x
# 	fig['selectedfigure']= True

# 	ground = random.choice(rigid_objects) # randomly pick an object
# 	print("ground = "+str(ground))

# 	ground.color += y
# 	ground['selectedground']= True









#  #select the object and make it active




# fig.select = True

# ### Create a duplicate
# bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False})

# ### Unlink the material and texture
# bpy.ops.object.make_single_user(object=False,obdata=False,material=True,texture=True,animation=False)

# ## Edit material of duplicate

# material = bpy.context.active_object.active_material

# material.type = "WIRE"

# material.use_object_color = False

# material.use_mist = False

# material.diffuse_color = [0.8,0,0]

# material.use_tangent_shading = True

# material.use_shadeless = True

# # Remove texture

# material.use_textures[0] = False

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
