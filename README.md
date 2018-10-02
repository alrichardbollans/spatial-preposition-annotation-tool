# Spatial Preposition Annotation Tool for Virtual Environments 

### Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Creating Annotations](#creating-annotations)
4. [Continuing Developments](#continuing-developments)
5. [Troubleshooting](#troubleshooting)
6. [Requirements](#requirements)
7. [Contact](#contact)

### Introduction

The aim of this tool is to allow for the collection of large amounts of rich data regarding how people use spatial prepositions in situated discourse.

The tool uses Blender's game engine and allows users to navigate environments, select objects and assign spatial prepositions relating pairs of objects. 

The tool is easily extendable to include various different tasks which bring out different aspects of the semantics and pragmatics of spatial preposition use.

By using virtual environments it is possible to extract large amounts of detailed information from the scene.


### Getting Started

#### Creating Scenes

The first thing you need is a set of scenes to work with. These should be stored in /blender/scene creation/scenes. Please avoid using "-" in file names.

Once scenes have been created, run 'process_scenes.py' to create environments to annotate.

There are a couple of things to note when creating a scene. See below

##### Adding new objects

In order to be able to distinguish concrete objects (chair, bowl etc..) from blender entities necessary for the game (camera, empty etc..) we use the 'rigid body' property.

Therefore, when adding new objects to the scene make sure that is is set to be a rigid body (In the Render view, under physics properties click 'Rigid Body').

All objects need to have unique names, but Blender will force this anyway.

##### Adding new prepositions

Prepositions that you would like to include in the various tasks are contained in /bgui-scripts/textui.py. All you need to do is add/remove prepositions from `preposition_list`.

### Creating Annotations

After processing scenes, run create-annotations.py. This will ask for the name of the scene file you would like to use.

Running this will add annotations to the annotation list csv in /outputs/.

#### Interface

* Left click selects an object in tasks where user only selects one object. Else:
  * Left click = Select figure
  * Right click= Select ground
* Arrow keys = Move around
* Mouse movement = Look around
* Normal keyboard interface for typing descriptions. Enter Key confirms the input.
* Space Bar selects a new preposition (in tasks where the preposition is given)
* DEL key deselects everything and reselects highlighted objects


Currently there are five modes for annotating

#### Standard Task

The standard task allows the user free reign to select figure and ground objects and give a suitable preposition.

#### Preposition Selection

In the preposition selection task two objects in the scene are selected at random and the user is asked to give an appropriate preposition relating the two (Red highlighting denotes the *figure* and blue denotes the *ground*). If the user doesn't deem appropriate any of the given prepositions they can press DEL to change the objects and the preposition.

#### Figure & Ground Selection

In this task, a preposition is given and users can select figure and ground combinations which fit the preposition. Pressing Space Bar changes the preposition.

#### Figure Selection
In this task, a preposition is given as well as a highlighted ground object and users can select figure objects which fit this pair. Pressing Space Bar changes the preposition. Pressing DEL changes the preposition and ground.
#### Ground Selection
In this task, a preposition is given as well as a highlighted figure object and users can select ground objects which fit this pair. Pressing Space Bar changes the preposition. Pressing DEL changes the preposition and figure.

### Continuing Developments

* Adding additional tasks
* Minor tweaks to the UI
* Detailed property extraction
* Improving game running efficiency

### Troubleshooting

### Requirements

##### Blender 2.79

See https://www.blender.org/

##### Python 2.7

Installing Python is generally easy, and nowadays many Linux and UNIX distributions include a recent Python. Even some Windows computers (notably those from HP) now come with Python already installed.

For guidance installing Python on your machine see https://wiki.python.org/moin/BeginnersGuide/Download

###### Note
The BGUI module has been included in the appropriate directory in the repository. We recommend keeping the version that is included in our repository as we have made minor changes to it.

### Contact
If you have any comments, queries or want to ask about extensions of the tool to fit your needs dont hesitate to get in touch!

Email: mm15alrb@leeds.ac.uk
