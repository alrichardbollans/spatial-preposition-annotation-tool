# Spatial Preposition Annotation Tool for Virtual Environments 

### Table of Contents
1. [Introduction](#introduction)
2. [Continuing Developments](#continuing-developments)
3. [Getting Started](#getting-started)
4. [Creating Annotations](#creating-annotations)
5. [Troubleshooting](#troubleshooting)
6. [Requirements](#Requirements)

### Introduction
The aim of this tool is to allow for the collection of large amounts of rich data regarding how people use spatial prepositions.

The tool uses Blender's game engine and allows users to navigate environments, select objects and give spatial prepositions to describe the relationships.

By using virtual scenes we are able to extract large amounts of information about the relationships between objects in the scene.


### Getting Started
#### Creating Scenes
The first thing you need is a set of scenes to work with.

At the moment the scene set up is still quite particular. We have included an example.blend in the 'scenes' folder and we recommend using this as a template.
##### Adding new objects
In order to be able to distinguish concrete objects (chair, bowl etc..) from blender entities necessary for the game (camera, empty etc..) we use the 'rigid body' property.

Therefore, when adding new objects to the scene make sure that is is set to be a rigid body (In the Render view, under physics properties click 'Rigid Body').

##### Adding new prepositions
Prepositions are stored in a separate scene (Scene.001). In order to add new prepositions you can copy one of the existing prepositions an alter the text, make sure to:

1. Change the name of the new object to that of the preposition e.g. "in".
2. Assign a custom property called "preposition" to the object.

We also plan on improving how prepositions are handled.

### Creating Annotations
After processing scenes, run create-annotations.py. This will ask what type of task you would like to use and which scene you want to use.

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

### Requirements
1. Blender
2. Python 2
