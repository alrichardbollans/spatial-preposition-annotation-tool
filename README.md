# Spatial Preposition Annotation Tool for Virtual Environments 

### Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Creating Annotations](#creating-annotations)
4. [Continuing Developments](#continuing-developments)
5. [Troubleshooting](#troubleshooting)
6. [Requirements](#Requirements)

### Introduction

The aim of this tool is to allow for the collection of large amounts of rich data regarding how people use spatial prepositions.

The tool uses Blender's game engine and allows users to navigate environments, select objects and give spatial prepositions to describe the relationships.

By using virtual scenes we are able to extract large amounts of information about the relationships between objects in the scene.


### Getting Started

#### Creating Scenes

The first thing you need is a set of scenes to work with. These should be stored in /blender/scene creation/scenes. Please avoid using "-" in file names.

Once scenes have been created, run 'process_scenes.py' to create environments to annotate.

At the moment the scene set up is still quite particular. We have included an example.blend in the 'scenes' folder and we recommend using this as a template.

##### Adding new objects

In order to be able to distinguish concrete objects (chair, bowl etc..) from blender entities necessary for the game (camera, empty etc..) we use the 'rigid body' property.

Therefore, when adding new objects to the scene make sure that is is set to be a rigid body (In the Render view, under physics properties click 'Rigid Body').

All objects need to have unique names, but Blender will force this anyway.

##### Adding new prepositions

Prepositions are stored in a separate scene (Scene.001). In order to add new prepositions you can copy one of the existing prepositions and alter the text. To do this:

1. Start by making sure that you are using the Camera's perspective. Usually this is toggled with Numpad 0.
2. Select "above" object and "aboveText" simultaneously by clicking on them while holding shift
3. Press Shift + D to create a duplicate. Move this duplicate to somewhere appropriate in the view.
4. Change the name of the object to be the preposition you are adding e.g. 'near'
5. Edit the text object to be your new preposition.

We have included a screenshot of what everything should look like after adding 'near' in this way.

We also plan on improving how prepositions are handled.

### Creating Annotations

After processing scenes, run create-annotations.py. This will ask for the name of the scene file you would like to use.

Running this will add annotations to the annotation list csv in /outputs/.

#### Interface

* Left click = Select figure or preposition
* Right click= Select ground
* Arrow keys = Move around
* Mouse movement = Look around

Currently there are two modes for annotating

#### Standard Task

The standard task allows the user free reign to select figure and ground objects and a suitable preposition.

#### Preposition Selection

In the preposition selection task two objects in the scene are selected at random and the user is asked to select appropriate an appropriate preposition relating the two (Red highlighting denotes the *figure* and blue denotes the *ground*). If the user doesn't deem appropriate any of the given prepositions they can select 'Cancel' to change the objects.

### Continuing Developments

* Adding additional tasks
* TextUI/Improving preposition selection
* Detailed property extraction
* Improving game running efficiency

### Troubleshooting

### Requirements

* Blender 2.79
* Python 2.7
