# Maya API 2.0 Plug-in Template

import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds

# Inform Maya to use API 2.0
def maya_useNewApi():
	pass

# Initialize the plugin with MObject 
def initializePlugin(plugin):

	vendor = "Adam Fatka - adam.fatka@gmail.com"
	version = "1.0.0"

	om.MFnPlugin(plugin, vendor, version)

def uninitializePlugin(plugin):
	pass