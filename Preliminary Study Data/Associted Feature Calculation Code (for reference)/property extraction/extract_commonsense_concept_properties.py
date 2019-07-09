import requests
import nltk
import csv

from nltk.corpus import wordnet



import sys

import os

def get_project_directory():

    current_directory = os.getcwd()
    user_home = os.path.expanduser("~")

    if os.path.basename(current_directory) == "preposition-project":
        return current_directory
    elif os.path.basename(os.path.dirname(current_directory)) == "preposition-project":
        return os.path.dirname(current_directory)
    else:
        return user_home + '/Dropbox/Shared-Study/preposition-project'

project_path = get_project_directory()
output_path = project_path +'/property extraction/blender data/'
relationship_class_path = project_path + '/property extraction/'
class_path = project_path + '/post processing/'

sys.path.append(relationship_class_path)
sys.path.append(class_path)

from relationship import Relationship
from relationship import Property
from classes import Scenes

scenes = Scenes()

def clean_name(obj):
    if '.' in obj:
        clean_name = obj[:obj.find(".")]
    elif '_' in obj:
        clean_name = obj[:obj.find("_")]
    else: 
        clean_name = obj
    return clean_name.lower()


def extract_relation_weight(relation,obj1,obj2):
	object1_name = clean_name(obj1)
	object2_name = clean_name(obj2)
	tag = '/r/'+relation
	
	conceptlinks = requests.get('http://api.conceptnet.io/query?node=/c/en/'+object1_name+'&other=/c/en/'+ object2_name).json()
	if len(conceptlinks['edges']) == 0:
		return 0
	elif not any(edges['rel']['@id'] == tag for edges in conceptlinks['edges']):
		return 0
	else:	
		for edges in conceptlinks['edges']:
			if edges['rel']['@id'] == tag:
				return edges['weight']

# def extract_isa_weight(obj1,obj2):
# 	object1_name = clean_name(obj1)
# 	object2_name = clean_name(obj2)
	
# 	conceptlinks = requests.get('http://api.conceptnet.io/query?node=/c/en/'+object1_name+'&other=/c/en/'+ object2_name).json()
# 	if len(conceptlinks['edges']) == 0:
# 		return 0
# 	for edges in conceptlinks['edges']:
# 		if edges['rel']['@id'] == '/r/IsA':
# 			return edges['weight']

# def extract_relatedto_weight(obj1,obj2):
# 	object1_name = clean_name(obj1)
# 	object2_name = clean_name(obj2)
	
# 	conceptlinks = requests.get('http://api.conceptnet.io/query?node=/c/en/'+object1_name+'&other=/c/en/'+ object2_name).json()
# 	if len(conceptlinks['edges']) == 0:
# 		return 0
# 	elif not any(edges['rel']['@id'] == '/r/RelatedTo' for edges in in conceptlinks['edges']):
# 		return 0
# 	else:	
# 		for edges in conceptlinks['edges']:
# 			if edges['rel']['@id'] == '/r/RelatedTo':
# 				return edges['weight']

# def extract_usedfor_weight(obj1,obj2):
# 	object1_name = clean_name(obj1)
# 	object2_name = clean_name(obj2)
	
# 	conceptlinks = requests.get('http://api.conceptnet.io/query?node=/c/en/'+object1_name+'&other=/c/en/'+ object2_name).json()
# 	if len(conceptlinks['edges']) == 0:
# 		return 0
# 	elif not any(edges['rel']['@id'] == '/r/UsedFor' for edges in in conceptlinks['edges']):
# 		return 0
# 	else:	
# 		for edges in conceptlinks['edges']:
# 			if edges['rel']['@id'] == '/r/UsedFor':
# 				return edges['weight']

		


# extract_isa_weight('mug','container')
# extract_relatedto_weight('mug','container')


def extract_path_similarity(obj1,obj2):
	object1_name = clean_name(obj1) + '.n.01'
	object2_name = clean_name(obj2) + '.n.01'

	x = wordnet.synset(object1_name)
	y = wordnet.synset(object2_name)

	return x.path_similarity(y)
#print(wordnet.synset('container.n.01'))
# container = wordnet.synset('mug.n.01')
# mug = wordnet.synset('container.n.01')

# print(container.path_similarity(mug))
# print(extract_path_similarity('mug','container'))
# print(extract_path_similarity('container','mug'))

for scene in scenes.scene_list:
	for obj in scenes.rigid_bodies[scene]:
		try:
			pr = Property(scene,obj)
			pr.set_of_properties['CN_ISA_CONTAINER'] = extract_relation_weight('IsA',clean_name(obj),'container')
			pr.set_of_properties['CN_UsedFor_Light'] = extract_relation_weight('UsedFor',clean_name(obj),'light')
			pr.save_to_csv(output_path)
		except:
			print('Commonsense property error')
			print(clean_name(obj))


# with open('commonsense properties.csv', "w") as csvfile:
#     outputwriter = csv.writer(csvfile)
#     outputwriter.writerow(['Object','CN_ISA_CONTAINER','CN_RelatedTo_CONTAINER','WNPathSimilarity_Container'])

# scene_list = scenes.scene_list
# for obj in scenes.distinct_bodies:
# 	CN_ISA_CONTAINER = extract_isa_weight(obj,'container')
# 	CN_RelatedTo_CONTAINER = extract_relatedto_weight(obj,'container')
# 	WNPathSimilarity_Container = extract_path_similarity(obj,'container')
# 	with open('commonsense properties.csv', "a") as csvfile:
# 	    outputwriter = csv.writer(csvfile)
# 	    outputwriter.writerow([obj,CN_ISA_CONTAINER,CN_RelatedTo_CONTAINER,WNPathSimilarity_Container])

# print(wordnet.synset('mug.n.01').definition())

### Testing

# concept = requests.get('http://api.conceptnet.io/query?node=/c/en/mug&other=/c/en/container').json()

# # print(concept['edges'])


# for edges in concept['edges']:
# 	if edges['rel']['@id'] == '/r/IsA':
# 		print(edges['weight'])
