import bpy

for t in bpy.data.images:
	if 'atp' in t.filepath:
		t.filepath = t.filepath.replace('/home/atp/Dropbox/Shared-Study/preposition-project/','//../../../')