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

### Instructions for Subjects

The aim of this tool is to collect data on how people use spatial prepositions.

Spatial prepositions are words or phrases like ‘in’, ‘on’, ‘above’, ‘to the right of’ etc.. 

In general they specify a (spatial) relation between two objects e.g. ‘the bike *to the left of* the house’.

Here we are interested in collecting examples of pairs of objects and prepositions that describe them. So for instance, two objects must be selected from the scene and you must give a preposition e.g. 'in' which describes the relation between the two objects.

Note: The objects that you will be able to select are in some sense atomic e.g. you can select the table in the scene but not specify a particular table leg; nor can you select the room which you are in but you can select various walls.

#### Some Important Terminology

The ‘figure’ is the object whose location is to be determined while the ‘ground’ is an object which is used as a point of reference or landmark. In general the structure of such phrases is: [Figure]+[Preposition]+[Ground]. So in the above example the bike is the figure and the house is the ground.


#### Note On Lag
We have recently made improvement which give big reductions in lag. If, however, excessive lag does occur usually moving the mouse away from clusters of objects will help.

#### Interface

* Left click selects an object in tasks where user only selects one object. Else:
  * Left click = Select figure
  * Right click= Select ground
* Arrow keys = Move around
* Mouse movement = Look around
* Normal keyboard interface for typing descriptions. Enter Key confirms the input.
* Space Bar selects a new preposition (in tasks where the preposition is already given)
* DEL key deselects everything and reselects highlighted objects
* ESC exits the game

In general green highlighting denotes a figure objects while red highlighting denotes a ground.

Currently there are five modes for annotating

#### Standard Task

In the standard task all you have to do is select a figure object (left click), a ground object (right click) and enter a preposition. Press enter to input your selections, if you make a mistake in any of your selections just press the delete key.

#### Preposition Selection

In the preposition selection task two objects in the scene are selected at random. All you have to do is enter a preposition which describes the pair. Note that green highlighting denotes the figure and red denotes the ground. If you can’t think of an appropriate preposition just press the delete key to change the pair of objects.


#### Figure & Ground Selection

In this task, a preposition is given at the top of the screen. What you have to do is select a figure (left click) and ground (right click). As soon as one figure is selected and one ground is selected the program will automatically input the selections. If you make a mistake in any of your selections just press the delete key. Pressing Space Bar changes the preposition.


#### Figure Selection
In this task, a preposition is given at the top of the screen as well as a highlighted ground object. You need to select figure objects which fit this pair e.g. if the highlighted ground is a bowl and the preposition is ‘in’ then you need to select all objects you think are in the bowl. Pressing Space Bar changes the preposition. Pressing the delete key changes the ground.
#### Ground Selection
In this task, a preposition is given at the top of the screen as well as a highlighted figure object. You need to select ground objects which fit this pair e.g. if the highlighted figure is a pencil and the preposition is ‘in’ then you need to select all objects that you think the pencil is in. Pressing Space Bar changes the preposition. Pressing the delete key changes the figure.

### Continuing Developments

* Adding additional tasks
* Minor tweaks to the UI
* Detailed property extraction

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
