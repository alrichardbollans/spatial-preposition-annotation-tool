import itertools

def clean_name(object_name):
	if '.' in object_name:
		clean_name = object_name[:object_name.find(".")]
	elif '_' in object_name:
		clean_name = object_name[:object_name.find("_")]
	else: 
		clean_name = object_name
	return clean_name.lower()

class SceneInfo:
	def __init__(self):
		
		self.scene_list = ['scene1.blend','scene2.blend','scene3.blend']
		self.rigid_bodies = {'scene1.blend':['Pencil.001', 'box.003', 'wall.003', 'wall.002', 'lamp.001', 'apple.003', 'light', 'Pencil.005', 'jar.001', 'Cube.001', 'box.002', 'box.001', 'box', 'spoon.002', 'balloon.001', 'ceiling', 'book.002', 'chair.003', 'chair.002', 'window.002', 'bin', 'guitar', 'chair.001', 'spoon.001', 'spoon', 'folder', 'Picture_001', 'apple.002', 'apple.001', 'Cube', 'Pencil.004', 'book.001', 'Pencil.003', 'book', 'wall.001', 'wall', 'shelf', 'lamp', 'jar', 'Pencil', 'plate', 'mug', 'bowl_001', 'Robot', 'dish', 'table', 'chair', 'cup', 'Table', 'chest', 'Floor']
	,'scene2.blend':['wall.003', 'banana.000', 'Cube.000', 'book.002', 'mug.002', 'notepad_001', 'light', 'book.001', 'book', 'wall.002', 'ceiling', 'bookshelf', 'box.001', 'spoon.001', 'Cube.002', 'Cube.001', 'box', 'chair.001', 'apple.008', 'window', 'door', 'apple.006', 'dish.001', 'jar.001', 'notebook.001', 'banana.004', 'spoon', 'Pencil.003', 'mug.001', 'folder', 'notebook', 'paper.002', 'table.001', 'ball.001', 'wall.001', 'wall', 'shelf', 'Pencil.001', 'ball', 'lamp', 'jar', 'mug', 'bowl_001', 'Robot', 'chair', 'cup', 'Table', 'Floor']
	,'scene3.blend':['wall.003', 'book.002', 'mug.002', 'notepad_001', 'light', 'book.001', 'book', 'wall.002', 'ceiling', 'bookshelf', 'box.001', 'spoon.001', 'Cube.002', 'Cube.001', 'apple.000', 'box', 'chair.001', 'pear.004', 'apple.009', 'apple.008', 'window', 'door', 'apple.006', 'dish.001', 'jar.001', 'notebook.001', 'banana.004', 'spoon', 'bowl', 'banana.001', 'Pencil.003', 'mug.001', 'folder', 'notebook', 'paper.002', 'table.001', 'ball.001', 'wall.001', 'wall', 'shelf', 'Pencil.001', 'ball', 'goblet', 'lamp', 'jar', 'mug', 'bowl_001', 'Robot', 'chair', 'cup', 'Table', 'Floor']
	}
	
		self.configs = self.get_all_configs()
		self.distinct_bodies = self.get_distinct_bodies()#['pencil', 'box', 'wall', 'lamp', 'apple', 'light', 'jar', 'cube', 'spoon', 'balloon', 'ceiling', 'book', 'chair', 'window', 'bin', 'guitar', 'folder', 'picture', 'shelf', 'plate', 'mug', 'bowl', 'robot', 'dish', 'table', 'cup', 'chest', 'floor', 'banana', 'notepad', 'bookshelf', 'door', 'notebook', 'paper', 'ball', 'pear', 'goblet']
	

	def get_distinct_bodies(self):
		collection = []
		for scene in self.scene_list:
			for obj in self.rigid_bodies[scene]:
				if clean_name(obj) not in collection:
					collection.append(clean_name(obj))
		return collection


	def get_all_configs(self):
		d = {}
		for scene in self.scene_list:
			x = list(itertools.permutations(self.rigid_bodies[scene], 2) )
			d[scene] = x
		return d


class Configuration:
	def __init__(self,scene,figure,ground):
		self.scene = scene
		self.figure = figure
		self.ground = ground
		self.row = []
		# This is the master list of value names. If this changes need to append and rewrite config data with compile instances.py
		self.value_names = ['figure_volume','figure_verticalness','figure_z_height','base_figure_movement_top','base_figure_movement_cobb','base_figure_movement_bottom','ground_volume','ground_verticalness','ground_z_height','ground_CN_ISA_CONTAINER','ground_CN_UsedFor_Light','distance','contact','contact_scaled','above_measure','shared_volume','containment','ins','raw_support_top','raw_support_cobb','raw_support_bottom','support_top','support_cobb','support_bottom','ground_CN_ISA_CONTAINER_Capped']
		# self.labelled = 0
	def __str__(self):
		return "["+str(self.scene)+","+str(self.figure)+","+str(self.ground)+"]"
	
	def append_values_from_instance(self,i):
		for v in self.value_names:
			value = getattr(i,v)
			setattr(self,v,value)
	def configuration_match(self,annotation):
		if self.scene == annotation.scene and self.figure == annotation.figure and self.ground == annotation.ground:
			return True
		else:
			return False
	def number_of_selections(self,preposition,datalist):
		counter = 0
		for an in datalist:
			if self.configuration_match(an) and an.preposition == preposition:
				counter += 1
		return counter
	def config_row_match(self,value):
		if self.scene == value[0] and self.figure == value[1] and self.ground == value[2]:
			return True
		else:
			return False
	def calculate_support_values(self,raw_value,base_movement):
				
		if raw_value <= 0:
			support = 0
		elif self.ground_z_height != 0:
			support = round((raw_value - base_movement)/self.ground_z_height, 4)
		else:
			support = round((raw_value - base_movement)/0.001, 4)

		if support > 1:
			support = 1

		return support
	def create_row(self):
		for value in self.value_names:	
			try:
				self.row.append(getattr(self,value))
			except Exception as e:
				self.row.append('?')
				print('Value not added')
				print('Figure: ' + self.figure)
				print('Ground: ' + self.ground)
				
				print('Scene: ' + self.scene)
				print('Value: ' + value)

				print(e)
	def print_info(self):
		print('Scene = ' + self.scene)
		print('Figure = ' + self.figure)
		print('Ground = ' + self.ground)


class Instance(Configuration):
	def __init__(self,ID,user,scene,preposition,figure,ground):
		Configuration.__init__(self,scene,figure,ground)
		self.preposition = preposition
		self.id = ID
		self.user = user
	def __str__(self):
		return "["+str(self.scene)+","+str(self.figure)+","+str(self.ground)+"]"
	def print_info(self):
		Configuration.print_info()
		print('preposition = ' + self.preposition)
		print('annotation id = ' + self.id)
		print('user = ' + self.user)

class SimplePragmaticInstance(Configuration):
	### Think about pluralisation
	thesaurus = [['mug','cup'],['ground','floor'],['desk','table']]
	def __init__(self,ID,user,scene,preposition,figure,ground,raw_sentence):
		Configuration.__init__(self,scene,figure,ground)
		self.possible_figures = self.get_possible_objects(self.figure)
		self.possible_grounds = self.get_possible_objects(self.ground)
		self.preposition = preposition
		self.id = ID
		self.user = user
		self.raw_sentence = raw_sentence

	def print_info(self):
		Configuration.print_info(self)
		print('preposition = ' + self.preposition)
		print('annotation id = ' + self.id)
		print('user = ' + self.user)

	def get_possible_objects(self,ground):
		out = []
		thesaurus_matches = [clean_name(ground)]
		s = SceneInfo()
		

		for x in self.thesaurus:
			if clean_name(ground) in x:
				for y in x:
					if y != clean_name(ground):
						thesaurus_matches.append(y)
		for obj in s.rigid_bodies[self.scene]:
			if clean_name(obj) in thesaurus_matches:
				out.append(obj)
		return out

	

# s = Scenes()

# s.get_all_configs()

# x = len(s.configs['scene1.blend']) + len(s.configs['scene2.blend']) + len(s.configs['scene3.blend'])

# y = len(s.rigid_bodies['scene1.blend']) + len(s.rigid_bodies['scene2.blend']) + len(s.rigid_bodies['scene3.blend'])
# print('Number of rigid_bodies')
# print(y)
# print('Number of configs:')
# print(x)