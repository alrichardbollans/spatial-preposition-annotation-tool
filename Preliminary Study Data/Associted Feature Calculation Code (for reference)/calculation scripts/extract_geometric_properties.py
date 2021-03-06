import sys

import os

module_path1 = os.getcwd() + '/add ons/'
module_path2 = os.getcwd() + '/scenes/add ons/'
# So we can find the bgui module
sys.path.append(module_path1)
sys.path.append(module_path2)

import blender_utils

import csv
import bpy

import itertools

from entity import Entity
from geometry_utils import *
from spatial import *

project_path = blender_utils.get_project_directory()
output_path = project_path +'/property extraction/blender data/'

relationship_class_path = project_path + '/property extraction/'

sys.path.append(relationship_class_path)

from relationship import Relationship
from relationship import Property


####################

scene = bpy.context.scene
scene_name = bpy.path.basename(bpy.context.blend_data.filepath)
#Average distance between entities in the scene
avg_dist = 0

rigid_body_list = blender_utils.create_list_rigid_bodies()

#### Create entity list and initialize entities
entities = []

for obj in rigid_body_list:
	ent = Entity(obj)
	entities.append(ent)
#### here is the function we want to make output the properties

def properties():

	for ent in entities:

		name = ent.name

		p = Property(scene_name,name)

		p.set_of_properties['volume'] = ent.volume
		if isVertical(ent):
			p.set_of_properties['verticalness'] = 1
		else:
			p.set_of_properties['verticalness'] = 0
		p.set_of_properties['z_height'] = ent.dimensions[2]

		p.save_to_csv(output_path)

def relations():

	for pair in itertools.permutations(entities, r = 2):
		ent1 = pair[0]
		ent2 = pair[1]

		figure = ent1.name
		ground = ent2.name

		r = Relationship(scene_name,figure,ground)

		## Get convex hulls
		# convexhull1 = Entity(ent1.convexhull)
		# convexhull2 = Entity(ent2.convexhull)

		### Get some distance measure
		r.set_of_relations['distance'] = dist_obj(ent1,ent2)

		### Measure the shortest distance between the meshes
		r.set_of_relations['contact'] = closest_mesh_distance(ent1, ent2)
		r.set_of_relations['contact_scaled'] = closest_mesh_distance_scaled(ent1, ent2)

		### Measure distance between highest point of entity 2 and lowest point of entity 1
		### Positive => ent1 is above ent2
		r.set_of_relations['above_measure'] = ent1.span[4] - ent2.span[5]

		### Measure the degree of containment
		#### Currently simple version using bounding boxes
		r.set_of_relations['shared_volume'] = get_bbox_intersection(ent1, ent2)
		### Proportion is divided by the figure volume i.e. if f in g then proportion = 1
		if ent1.volume == 0:
			r.set_of_relations['containment'] = r.set_of_relations['shared_volume'] / (ent1.volume + 0.0001)
		else:
			r.set_of_relations['containment'] = r.set_of_relations['shared_volume'] / ent1.volume
		if ent2.volume != 0:
			r.set_of_relations['ins'] = inside(ent1,ent2)
		else:
			r.set_of_relations['ins'] = 0

		
		r.save_to_csv(output_path)

properties()

relations()
# 	global avg_dist
# 	# if len(entities) != 0:
# 	# 	for pair in itertools.combinations(entities, r = 2):
# 	# 		avg_dist += dist_obj(pair[0], pair[1])
# 	# 	avg_dist = avg_dist * 2 / (len(entities) * (len(entities) - 1))

	
# 	####### output properties here
# 	for ent in entities:
# 		geomprop = GeometricProperties()
# 		geomprop.object1 = ent.name
# 		geomprop.volume = ent.volume

# 		### add properties to list
# 		with open(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))+'/outputs/object properties.csv', "a") as csvfile:
# 			outputwriter = csv.writer(csvfile)
# 			outputwriter.writerow([geomprop.scene,geomprop.object1,geomprop.volume])

# 	for pair in itertools.combinations(entities, r = 2): #THIS ASSUMES THE RELATIONS ARE SYMMETRIC
# 		geomrel = GeometricRelations()
# 		geomrel.object1 = pair[0].name
# 		geomrel.object2 = pair[1].name
# 		geomrel.distance = dist_obj(pair[0],pair[1])

# 		### add properties to list
# 		with open(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))+'/outputs/object relations.csv', "a") as csvfile:
# 			outputwriter = csv.writer(csvfile)
# 			outputwriter.writerow([geomrel.scene,geomrel.object1,geomrel.object2,geomrel.distance])
# main()


########### Following may be useful/necessary in future. Some should be added to geometry utils file




# #Computes the value of the univariate Gaussian
# #Inputs: x - random variable value; mu - mean; sigma - variance
# #Return value: real number
# def gaussian(x, mu, sigma):
# 	return e ** (- 0.5 * ((float(x) - mu) / sigma) ** 2) / (math.fabs(sigma) * math.sqrt(2.0 * pi))

# #Computes the value of the logistic sigmoid function
# #Inputs: x - random variable value; a, b - coefficients
# #Return value: real number
# def sigmoid(x, a, b):
# 	return a / (1 + e ** (- b * x)) if b * x > -100 else 0

# #Computes the normalized area of the intersection of projection of two entities onto the XY-plane
# #Inputs: a, b - entities
# #Return value: real number
# def get_proj_intersection(a, b):
# 	bbox_a = a.get_bbox()
# 	bbox_b = b.get_bbox()
# 	axmin = a.span[0]
# 	axmax = a.span[1]
# 	aymin = a.span[2]
# 	aymax = a.span[3]
# 	bxmin = b.span[0]
# 	bxmax = b.span[1]
# 	bymin = b.span[2]
# 	bymax = b.span[3]
# 	xdim = 0
# 	ydim = 0
# 	if axmin >= bxmin and axmax <= bxmax:
# 		xdim = axmax - axmin
# 	elif bxmin >= axmin and bxmax <= axmax:
# 		xdim = bxmax - bxmin
# 	elif axmin <= bxmin and axmax <= bxmax and axmax >= bxmin:
# 		xdim = axmax - bxmin
# 	elif axmin >= bxmin and axmin <= bxmax and axmax >= bxmax:
# 		xdim = bxmax - axmin

# 	if aymin >= bymin and aymax <= bymax:
# 		ydim = aymax - aymin
# 	elif bymin >= aymin and bymax <= aymax:
# 		ydim = bymax - bymin
# 	elif aymin <= bymin and aymax <= bymax and aymax >= bymin:
# 		ydim = aymax - bymin
# 	elif aymin >= bymin and aymin <= bymax and aymax >= bymax:
# 		ydim = bymax - aymin
# 	area = xdim * ydim
	
# 	#Normalize the intersection area to [0, 1]
# 	return e ** (area - min((axmax - axmin) * (aymax - aymin), (bxmax - bxmin) * (bymax - bymin)))
	
# #Returns the orientation of the entity relative to the coordinate axes
# #Inputs: a - entity
# #Return value: triple representing the coordinates of the orientation vector
# def get_planar_orientation(a):
# 	dims = a.get_dimensions()
# 	if dims[0] == min(dims):
# 		return (1, 0, 0)
# 	elif dims[1] == min(dims):
# 		return (0, 1, 0)
# 	else: return (0, 0, 1)


# #Returns the frame size of the current scene
# #Inputs: none
# #Return value: real number
# def get_frame_size():
# 	max_x = -100
# 	min_x = 100
# 	max_y = -100
# 	min_y = 100
# 	max_z = -100
# 	min_z = 100

# 	#Computes the scene bounding box
# 	for entity in entities:
# 		max_x = max(max_x, entity.span[1])
# 		min_x = min(min_x, entity.span[0])
# 		max_y = max(max_y, entity.span[3])
# 		min_y = min(min_y, entity.span[2])
# 		max_z = max(max_z, entity.span[5])
# 		min_z = min(min_z, entity.span[4])
# 	return max(max_x - min_x, max_y - min_y, max_z - min_z)




# #Computes the degree of vertical alignment (coaxiality) between two entities
# #The vertical alignment takes the max value if one of the objects is directly above the other
# #Inputs: a, b - entities
# #Return value: real number from [0, 1]
# def v_align(a, b):
# 	dim_a = a.get_dimensions()
# 	dim_b = b.get_dimensions()
# 	center_a = a.get_bbox_centroid()
# 	center_b = b.get_bbox_centroid()
# 	return gaussian(0.9 * point_distance((center_a[0], center_a[1], 0), (center_b[0], center_b[1], 0)) / 
# 								(max(dim_a[0], dim_a[1]) + max(dim_b[0], dim_b[1])), 0, 1 / math.sqrt(2*pi))

# #Computes the degree of vertical offset between two entities
# #The vertical offset measures how far apart are two entities one
# #of which is above the other. Takes the maximum value when one is
# #directly on top of another
# #Inputs: a, b - entities
# #Return value: real number from [0, 1]
# def v_offset(a, b):
# 	dim_a = a.get_dimensions()    
# 	dim_b = b.get_dimensions()
# 	center_a = a.get_bbox_centroid()
# 	center_b = b.get_bbox_centroid()
# 	h_dist = math.sqrt((center_a[0] - center_b[0]) ** 2 + (center_a[1] - center_b[1]) ** 2)    
# 	return gaussian(2 * (center_a[2] - center_b[2] - 0.5*(dim_a[2] + dim_b[2])) /  \
# 					(1e-6 + dim_a[2] + dim_b[2]), 0, 1 / math.sqrt(2*pi))

	
#The following functions are for precomputing the corresponding
#relation for every pair of entities
#
#

# def compute_at(entities):
# 	obj = [[x, [y for y in entities if x != y and near(y, x) > 0.8]] for x in entities]
# 	return "\n".join(", ".join(y.name for y in x[1]) + " is at the " + x[0].name for x in obj if x[1] != [])

# def compute_near(entities):
# 	obj = [[x, [y for y in entities if x != y and near(y, x) > 0.6]] for x in entities]
# 	return "\n".join(", ".join(y.name for y in x[1]) + " is near the " + x[0].name for x in obj if x[1] != [])

# def compute_on(entities):
# 	obj = [[x, [y for y in entities if x != y and on(y, x) > 0.8]] for x in entities]
# 	return "\n".join(", ".join(y.name for y in x[1]) + " is on the " + x[0].name for x in obj if x[1] != [])

# def compute_above(entities):
# 	obj = [[x, [y for y in entities if x != y and above(y, x) > 0.7]] for x in entities]
# 	return "\n".join(", ".join(y.name for y in x[1]) + " is above the " + x[0].name for x in obj if x[1] != [])

# def compute_below(entities):
# 	obj = [[x, [y for y in entities if x != y and below(y, x) > 0.7]] for x in entities]
# 	return "\n".join(", ".join(y.name for y in x[1]) + " is below the " + x[0].name for x in obj if x[1] != [])

# def compute_over(entities):
# 	obj = [[x, [y for y in entities if x != y and over(y, x) > 0.7]] for x in entities]
# 	return "\n".join(", ".join(y.name for y in x[1]) + " is over the " + x[0].name for x in obj if x[1] != [])

#

'''
def gen_data(func_name):
	pos = 100.0
	neg = 100.0
	data = open(func_name + ".train", "w")
	index = 0
	for pair in itertools.permutations(entities, r = 2):
		if index < 1000:
			a, b = pair
			if a.name != 'plane' and b.name != 'plane':
				a_bbox_str = " ".join([" ".join([str(x) for x in y]) for y in a.get_bbox()])
				b_bbox_str = " ".join([" ".join([str(x) for x in y]) for y in b.get_bbox()])
				a_cen = a.get_bbox_centroid()
				b_cen = b.get_bbox_centroid()
				outstr = a_bbox_str + " " + b_bbox_str #" ".join([str(x) for x in a_cen]) + " " + " ".join([str(x) for x in b_cen])            
				if globals()[func_name](a, b) > 0.7: # and float(pos) / (pos + neg) <= 0.6:
					outstr = outstr + " 1\n"
					#pos = pos + 1
					data.write(outstr)
				else: #if neg / (pos + neg) <= 0.6:
					outstr = outstr + " -1\n"
					#neg = neg + 1
					data.write(outstr)
				index = index + 1
	data.close()
''' 

#Creates and configures the special "observer" object
#(which is just a camera). Needed for deictic relations as
#well as several other aspects requiring the POV concept,
#e.g., taking screenshots.
#Inputs: none
#Return value: the camera object
# def get_observer():
# 	lamp = bpy.data.lamps.new("Lamp", type = 'POINT')
# 	lamp.energy = 30
# 	cam = bpy.data.cameras.new("Camera")

# 	if bpy.data.objects.get("Lamp") is not None:
# 		lamp_obj = bpy.data.objects["Lamp"]
# 	else:
# 		lamp_obj = bpy.data.objects.new("Lamp", lamp)
# 		scene.objects.link(lamp_obj)
# 	if bpy.data.objects.get("Camera") is not None:
# 		cam_ob = bpy.data.objects["Camera"]
# 	else:
# 		cam_ob = bpy.data.objects.new("Camera", cam)
# 		scene.objects.link(cam_ob)    

# 	lamp_obj.location = (-20, 0, 10)
# 	cam_ob.location = (-15.5, 0, 7)
# 	cam_ob.rotation_mode = 'XYZ'
# 	cam_ob.rotation_euler = (1.1, 0, -1.57)
# 	bpy.data.cameras['Camera'].lens = 20
	
# 	bpy.context.scene.camera = scene.objects["Camera"]


# 	if bpy.data.objects.get("Observer") is None:
# 		mesh = bpy.data.meshes.new("Observer")
# 		bm = bmesh.new()
# 		bm.verts.new(cam_ob.location)
# 		bm.to_mesh(mesh)
# 		observer = bpy.data.objects.new("Observer", mesh)    
# 		scene.objects.link(observer)
# 		bm.free()
# 		scene.update()
# 	else: 
# 		observer = bpy.data.objects["Observer"]            
# 	observer_entity = Entity(observer)
# 	observer_entity.camera = cam_ob
# 	return observer_entity

# #Searches and returns the entity that has the given name
# #associated with it
# #Inputs: name - human-readable name as a string
# #Return value: entity (if exists) or None
# def get_entity_by_name(name):
# 	for entity in entities:
# 		#print("NAME:",name, entity.name)
# 		if entity.name.lower() == name.lower():
# 			return entity
# 	for col in color_mods:
# 		if col in name:
# 			name = name.replace(col + " ", "")
# 			#print ("MOD NAME:", name)
# 	for entity in entities:
# 		#print(name, entity.name)
# 		if entity.name.lower() == name.lower():
# 			return entity
# 	return None

# #Places the entity at a specified location and with specified orientation
# #Inputs: entity, position - triple of point coordinates, rotation - triple of Euler angles
# #Return value: none
# def place_entity(entity, position=(0,0,0), rotation=(0,0,0)):
# 	obj = entity.constituents[0]
# 	obj.location = position
# 	obj.rotation_mode = 'XYZ'
# 	obj.rotation_euler = rotation
# 	scene.update()

# #Places the set of entities within a certain region 
# #Inputs: reg - the bounding box of the region, collection - list of entities
# #Return value: none
# def arrange_entities(reg, collection):
# 	for entity in collection:
# 		if entity.get('fixed') is None:
# 			#print (entity.name)
# 			if reg[4] == reg[5]:
# 				pos = (random.uniform(reg[0], reg[1]), random.uniform(reg[2], reg[3]), reg[4])#entity.get_parent_offset()[2])
# 			else:
# 				pos = (random.uniform(reg[0], reg[1]), random.uniform(reg[2], reg[3]), random.uniform(reg[4], reg[5]))
# 			place_entity(entity, pos, (math.pi,0,0))
# 			while check_collisions(entity):
# 				print (entity.name, pos)
# 				if reg[4] == reg[5]:
# 					pos = (random.uniform(reg[0], reg[1]), random.uniform(reg[2], reg[3]), reg[4])#entity.get_parent_offset()[2])
# 				else:
# 					pos = (random.uniform(reg[0], reg[1]), random.uniform(reg[2], reg[3]), random.uniform(reg[4], reg[5]))
# 				place_entity(entity, pos, (math.pi,0,0))

# #Checks if the projections of two entities onto a coordinate axis "collide" (overlap)
# #Inputs: int_a, int_b - the projections of two entities as intervals (pairs of numbers)
# #Return value: Boolean value                
# def axis_collision(int_a, int_b):
# 	return int_a[1] <= int_b[1] and int_a[1] >= int_b[0] or \
# int_a[0] >= int_b[0] and int_a[0] <= int_b[1] or \
# int_b[0] >= int_a[0] and int_b[0] <= int_a[1] or \
# int_b[1] >= int_a[0] and int_b[1] <= int_a[1]

# #Checks if the entity "collides" (overlaps) with some other entity along any coordinate axis
# #Inputs: a - entity
# #Return value: Boolean value                
# def check_collisions(a):
# 	for entity in entities:
# 		if entity != a and check_collision(a, entity):
# 			print (entity.name, a.name)
# 			return True
# 	return False            

#Checks if two entities "collide" (overlap) along some coordinate axis
#Inputs: a,b - entities
#Return value: Boolean value                
# def check_collision(a, b):
# 	span_a = a.get_span()
# 	span_b = b.get_span()
# 	return axis_collision((span_a[0], span_a[1]), (span_b[0], span_b[1])) and \
# 						  axis_collision((span_a[2], span_a[3]), (span_b[2], span_b[3])) and \
# 						  axis_collision((span_a[4], span_a[5]), (span_b[4], span_b[5]))

#STUB
# def put_on_top(a, b):
# 	pass


# #Render and save the current scene screenshot
# #Inputs: none
# #Return value: none
# def save_screenshot():
# 	add_props()
# 	scene.render.resolution_x = 1920
# 	scene.render.resolution_y = 1080
# 	scene.render.resolution_percentage = 100
# 	scene.render.use_border = False
# 	scene.render.image_settings.file_format = 'JPEG'
# 	current_scene = bpy.data.filepath.split("/")[-1].split(".")[0]
# 	scene.render.filepath = filepath + current_scene + ".jpg"
# 	bpy.ops.render.render(write_still=True)

# #Given the relations argument specification, returns the entities that
# #satisfy that specification
# #Inputs: arg - argument object
# #Return value: the list of entities
# def get_argument_entities(arg):
# 	ret_val = [get_entity_by_name(arg.token)]
# 	if ret_val == [None]:
# 		ret_val = []
# 		for entity in entities:            
# 			#print ("TYPE_STR: {} {}".format(entity.name, entity.type_structure))
# 			if (entity.type_structure is None):
# 				print ("NONE STRUCTURE", entity.name)                
# 			if (arg.token in entity.type_structure or arg.token in entity.name.lower() or arg.token == "block" and "cube" in entity.type_structure) \
# 			   and (arg.mod is None or arg.mod.adj is None or arg.mod.adj == "" or entity.color_mod == arg.mod.adj or arg.mod.adj in entity.type_structure[-1].lower()):
# 				ret_val += [entity]    
# 	return ret_val

# #Computes the projection of an entity onto the observer's visual plane
# #Inputs: entity - entity, observer - object, representing observer's position
# #and orientation
# #Return value: list of pixel coordinates in the observer's plane if vision
# def vp_project(entity, observer):
# 	points = reduce((lambda x,y: x + y), [[obj.matrix_world * v.co for v in obj.data.vertices] for obj in entity.constituents if (obj is not None and hasattr(obj.data, 'vertices') and hasattr(obj, 'matrix_world'))])   
# 	co_2d = [bpy_extras.object_utils.world_to_camera_view(scene, observer.camera, point) for point in points]
# 	render_scale = scene.render.resolution_percentage / 100
# 	render_size = (int(scene.render.resolution_x * render_scale), int(scene.render.resolution_y * render_scale),)
# 	pixel_coords = [(round(point.x * render_size[0]),round(point.y * render_size[1]),) for point in co_2d]
# 	return pixel_coords


# #Filters the entities list according to the set of constraints, i.e.,
# #returns the list of entities satisfying certain criteria
# #Inputs: entities - list of entities; constaints - list of constraints in the
# #form (type, value), e.g., (color_mod, 'black')
# #Return value: list of entities
# def filter(entities, constraints):
# 	result = []
# 	for entity in entities:
# 		isPass = True
# 		for cons in constraints:
# 			#print("TYPE_STR:", entity.name, entity.get_type_structure())
# 			if cons[0] == 'type' and entity.get_type_structure()[-2] != cons[1]:
# 				isPass = False
# 			elif cons[0] == 'color_mod' and entity.color_mod != cons[1]:
# 				isPass = False
# 		if isPass:
# 			result.append(entity)
# 	return result


#For a description task, finds the best candiadate entity
#Inputs: relation - relation name (string), rel_constraints - the list of constraints
#imposed on the relatum, referents - the list of referent entities
#Return value: the best candidate entity
# def eval_find(relation, rel_constraints, referents):
# 	candidates = filter(entities, rel_constraints)
# 	print ("CANDIDATES: {}".format(candidates))
# 	scores = []
# 	if len(referents[0]) == 1 or relation == "between":
# 		scores = [(cand, cand.name, max([globals()[rf_mapping[relation]](cand, *ref) for ref in referents if cand not in ref])) for cand in candidates]
# 	else:
# 		scores = [(cand, cand.name, max([np.mean([globals()[rf_mapping[relation]](cand, ref) for ref in refset]) for refset in referents if cand not in refset])) for cand in candidates]
# 	print ("SCORES: {}".format(scores))
# 	max_score = 0
# 	best_candidate = None
# 	for ev in scores:
# 		if ev[2] > max_score:
# 			max_score = ev[2]
# 			best_candidate = ev[0]
# 	return best_candidate

# #Processes a truth-judgement annotation
# #Inputs: relation, relatum, referent1, referent2 - strings, representing
# #the relation and its arguments; response - user's response for the test
# #Return value: the value of the corresponding relation function
# # def process_truthjudg(relation, relatum, referent1, referent2, response):
# #     relatum = get_entity_by_name(relatum)
# #     referent1 = get_entity_by_name(referent1)
# #     referent2 = get_entity_by_name(referent2)
# #     print (relatum, referent1, referent2)
# #     if relation != "between":
# #         return globals()[rf_mapping[relation]](relatum, referent1)
# #     else: return globals()[rf_mapping[relation]](relatum, referent1, referent2)

# #Extracts the constraints (type and color) for the relatum argument
# #from the parsing result.
# #Inputs: relatum - string, representing the relation argument;
# #rel_constraints - the type and color properties of the relatum
# #Return value: The list of pairs ('constraint_name', 'constraint_value')
# def get_relatum_constraints(relatum, rel_constraints):
# 	ret_val = [('type', relatum.get_type_structure()[-2]), ('color_mod', relatum.color_mod)]
# 	return ret_val

#Processes a description-tast annotation
#Inputs: relatum - string, representing the relation argument;
#response - user's response for the test
#Return value: the best-candidate entity fo the given description
# def process_descr(relatum, response):
#     rel_constraint = parse(response)
#     if rel_constraint is None:
#         return None
#     relatum = get_entity_by_name(relatum)
#     #print ("REF: {}".format(rel_constraint.referents))
#     if rel_constraint is None:
#         return "*RESULT: NO RELATIONS*"
#     referents = list(itertools.product(*[get_argument_entities(ref) for ref in rel_constraint.referents]))
#     print("REFS:", referents)
#     relation = rel_constraint.token
#     return eval_find(relation, get_relatum_constraints(relatum, rel_constraint), referents)

# def scaled_axial_distance(a_bbox, b_bbox):
# 	a_span = (a_bbox[1] - a_bbox[0], a_bbox[3] - a_bbox[2])
# 	b_span = (b_bbox[1] - b_bbox[0], b_bbox[3] - b_bbox[2])
# 	a_center = ((a_bbox[0] + a_bbox[1]) / 2, (a_bbox[2] + a_bbox[3]) / 2)
# 	b_center = ((b_bbox[0] + b_bbox[1]) / 2, (b_bbox[2] + b_bbox[3]) / 2)
# 	axis_dist = (a_center[0] - b_center[0], a_center[1] - b_center[1])
# 	return (2 * axis_dist[0] / max(a_span[0] + b_span[0], 2), 2 * axis_dist[1] / max(a_span[1] + b_span[1], 2))

# def get_weighted_measure(a, b, observer):
# 	a_bbox = get_2d_bbox(vp_project(a, observer))
# 	b_bbox = get_2d_bbox(vp_project(b, observer))
# 	axial_dist = scaled_axial_distance(a_bbox, b_bbox)
# 	if axial_dist[0] <= 0:
# 		return 0
# 	horizontal_component = sigmoid(axial_dist[0], 1.0, 0.5) - 0.5
# 	vertical_component = gaussian(axial_dist[1], 0, 2.0)
# 	distance_factor = math.exp(-0.01 * axial_dist[0])
# 	return 0.5 * horizontal_component + 0.3 * vertical_component + 0.2 * distance_factor



# def fix_ids():
# 	for ob in scene.objects:
# 		if ob.get('main') is not None:# and ob.get('id') is None:
# 			for key in types_ids.keys():
# 				if key in ob.name.lower():
# 					ob['id'] = types_ids[key] + "." + ob.name
# 			if ob.get('color_mod') is None:
# 				for color in color_mods:
# 					if color in ob.name.lower():
# 						ob['color_mod'] = color
# 						break

# def get_similar_entities(relatum):
# 	ret_val = []
# 	relatum = get_entity_by_name(relatum)
# 	for entity in entities:
# 		if relatum.type_structure[-2] == entity.type_structure[-2] and (relatum.color_mod is None \
# 		   and entity.color_mod is None or relatum.color_mod == entity.color_mod):
# 			ret_val += [entity]
# 	return ret_val

# def pick_descriptions(relatum):
# 	candidates = get_similar_entities(relatum)
# 	relatum = get_entity_by_name(relatum)
# 	max_vals = []
# 	for relation in relations:
# 		max_val = 0
# 		if relation != 'between':            
# 			for ref in entities:
# 				if ref != relatum:
# 					max_val = max([(globals()[rf_mapping[relation]](cand, ref), cand) for cand in candidates], key=lambda arg: arg[0])
# 		else:
# 			for pair in itertools.combinations(entities, r = 2):
# 				if relatum != pair[0] and relatum != pair[1]:
# 					max_val = max([(globals()[rf_mapping[relation]](cand, pair[0], pair[1]), cand) for cand in candidates], key=lambda arg: arg[0])
# 		if max_val[1] == relatum:
# 			max_vals += [(relation, max_val[0])]
# 	max_vals.sort(key=lambda arg: arg[1])
# 	print ("MAX_VALS: {}".format(max_vals))
# 	max_vals = [item[0] for item in max_vals]
# 	return tuple(max_vals[0:3])

#The observer object (camera)
#observer = get_observer()

# def get_entities():
# 	print (entities)
# 	return entities



# if __name__ == "__main__":
# 	#save_screenshot()
# 	#fix_ids()
# 	#bpy.ops.wm.save_mainfile(filepath=bpy.data.filepath)
# 	main()  