# Spatial Preposition Annotation Tool for Virtual Environments 

### Table of Contents
1. [Introduction](#introduction)
2. [Continuing Developments](#continuing-developments)
2. [Getting Started](#getting-started)
3. [Troubleshooting](#troubleshooting)

### Introduction
The aim of this tool is to allow for the collection of large amounts of rich data regarding how people use spatial prepositions.

The tool uses Blender's game engine and allows users to navigate environments, select objects and give spatial prepositions to describe the relationships.

By using virtual scenes we are able to extract large amounts of information about the relationships between objects in the scene.

### Requirements
1. Blender
2. Python 2

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

### Continuing Developments
* Adding additional tasks
* TextUI/Improving preposition selection
* Detailed property extraction
* Improving game running efficiency
