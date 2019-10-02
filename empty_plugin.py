# Maya API 2.0 Plug-in Template

import maya.api.OpenMaya as om
import maya.cmds as cmds

# Inform Maya to use API 2.0
def maya_useNewAPI():
	pass

# maya_useNewApi = True

# Initialize the plugin with MObject 
def initializePlugin(plugin):

	vendor = "Adam Fatka - adam.fatka@gmail.com"
	version = "1.0.0"

	om.MFnPlugin(plugin, vendor, version)

def uninitializePlugin(plugin):
	pass

if __name__ == "__main__":
	plugin_name = "empty_plugin.py"

	cmds.evalDeferred("If cmds.pluginInfo('{0}', query = True, loaded = True): cmds.unloadPlugin('{0}')".format(plugin_name)
	cmds.evalDeferred("If not cmds.pluginInfo('{0}', query = True, loaded = True): cmds.loadPlugin('{0}')".format(plugin_name)