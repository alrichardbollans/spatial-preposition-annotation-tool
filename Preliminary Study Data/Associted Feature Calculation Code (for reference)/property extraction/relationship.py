import csv
class Relationship:
	### Add relations at end of list otherwise they may get overwritten
	## Describe each key here
	# Distance: Closest face distance from one object to centre of the other
	# Contact: the closest distance between the points of two meshes
	# Contact Scaled: Contact scaled by the maximum dimensions of two entities
	# above_measure: distance between highest point of entity 2 and lowest point of entity 1
	# shared_volume: he shared volume of the bounding boxes of two entities
	# containment: shared volume divided by volume of figure
	# ins: Platonov's inside measure
	# 'raw_support:top_change': the change in highest point of figure when the ground is removed 
	#'raw_support:cobb_change': the change in centre of bounding box of figure when the ground is removed
	#'raw_support:bottom_change': the change in lowest point of figure when the ground is removed
	relation_keys = ['distance','contact','contact_scaled','above_measure','shared_volume','containment','ins','raw_support:top_change','raw_support:cobb_change','raw_support:bottom_change']

	
	def __init__(self,scene,figure,ground):
		self.scene = scene
		self.figure = figure
		self.ground = ground
		self.set_of_relations = {}

	def load_from_csv(self,filepath):
		with open(filepath +"relations.csv", "r") as f:
			reader = csv.reader(f)     # create a 'csv reader' from the file object
			geom_relations = list( reader )  # create a list from the reader		
			
		for relation in geom_relations:
			if self.scene == relation[0] and self.figure == relation[1] and self.ground == relation[2]:
				# print(geom_relations.index(relation))
				for r in self.relation_keys:
					if relation[self.relation_keys.index(r)+3] != '?':
						self.set_of_relations[r] =float(relation[self.relation_keys.index(r)+3])
					else:
						self.set_of_relations[r] = '?'

	def save_to_csv(self,output_path):
		# self.load_from_csv(output_path)

		row = [self.scene,self.figure,self.ground]

		for r in self.relation_keys:
			if r in self.set_of_relations:
				row.append(self.set_of_relations[r])
			else:
				row.append('?')
				self.set_of_relations[r] = '?'
		
		with open(output_path + 'relations.csv') as incsvfile:
			read = csv.reader(incsvfile) #.readlines())
			reader = list(read)

			if any(self.scene == line[0] and self.figure == line[1] and self.ground == line[2] for line in reader):
				try:
					with open(output_path + 'relations.csv', "w") as csvfile:
						outputwriter = csv.writer(csvfile)
						titles = ['scene','figure','ground'] + self.relation_keys
						outputwriter.writerow(titles)
						for line in reader[:]:
							if 'scene' not in line:
								if self.scene == line[0] and self.figure == line[1] and self.ground == line[2]:
									### Must ofset by 3 here due to each row beginning with scene and object names
									for x in range(0,len(self.relation_keys)):
										
										if self.set_of_relations[self.relation_keys[x]] != '?':
											if len(line) > x+3:
												line[x+3] = self.set_of_relations[self.relation_keys[x]]
											else:
												line.append(self.set_of_relations[self.relation_keys[x]])
									
									

								outputwriter.writerow(line)
				except Exception as e:

					print('Writing to CSV Failed')
					print('Figure: ' + self.figure)
					print('Ground:' + self.ground)
					print(e)
			else:
				with open(output_path + 'relations.csv', "a") as csvfile:
					outputwriter = csv.writer(csvfile)
					outputwriter.writerow(row)
#### add various calculations here
	

class Property:
	### Add relations at end of list otherwise they may get overwritten
	#volume: volume of bounding box
	# verticalness: Checks whether the entity is vertically oriented
	# z_height: span in z dimension
	# base_movemnt: z movement of object in scene (wih no changes)
	# CN_ISA_CONTAINER: ConeceptNet IsA container weight

	property_keys = ['volume','verticalness','z_height','base_movement:top','base_movement:cobb','CN_ISA_CONTAINER','base_movement:bottom','CN_UsedFor_Light']
	
	def __init__(self,scene,object_name):
		self.scene = scene
		self.name = object_name
		self.set_of_properties = {}

	def save_to_csv(self,output_path):

		row = [self.scene,self.name]

		for r in self.property_keys:
			if r in self.set_of_properties:
				row.append(self.set_of_properties[r])
			else:
				row.append('?')
				self.set_of_properties[r] = '?'

		with open(output_path + 'properties.csv') as incsvfile:
			read = csv.reader(incsvfile)
			reader = list(read)
			if any(self.scene == line[0] and self.name == line[1] for line in reader):
				try:
					with open(output_path + 'properties.csv', "w") as csvfile:
						outputwriter = csv.writer(csvfile)
						titles = ['scene','object'] + self.property_keys	
						outputwriter.writerow(titles)
						
						for line in reader[:]:
							if 'scene' not in line:
								if self.scene == line[0] and self.name == line[1]:
									### Must ofset by 2 here due to each row beginning with scene and name
									for x in range(0,len(self.property_keys)):
										
										if self.set_of_properties[self.property_keys[x]] != '?':
											if len(line) > x+2:
												line[x+2] = self.set_of_properties[self.property_keys[x]]
											else:
												line.append(self.set_of_properties[self.property_keys[x]])

								outputwriter.writerow(line)
				except Exception as e:
					print('Writing to CSV Failed')
					print('Object: ' + self.name)
					
					print(e)

			else:
				with open(output_path + 'properties.csv', "a") as csvfile:
					outputwriter = csv.writer(csvfile)
					outputwriter.writerow(row)

	def load_from_csv(self,filepath):
		with open(filepath + "properties.csv", "r") as f:
			reader = csv.reader(f)     # create a 'csv reader' from the file object
			geom_props = list( reader )  # create a list from the reader		
			
		for prop in geom_props:
			if self.scene == prop[0] and self.name == prop[1]:
				for r in self.property_keys:
					if prop[self.property_keys.index(r)+2] not in ['?','']:
						self.set_of_properties[r] =float(prop[self.property_keys.index(r)+2])
					else:
						self.set_of_properties[r] = '?'

