# Maya API 2.0 Plug-in Template

import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui 

import maya.cmds as cmds

# Inform Maya to use API 2.0
def maya_useNewAPI():
	pass

class HelloWorldNode(omui.MPxLocatorNode):

	TYPE_NAME = "helloworld"
	TYPE_ID = om.MTypeId(0x0007f7f7)

	def __init__(self):
		super(HelloWorldNode, self).__init__()


	@classmethod
	def creator(cls):
		return HelloWorldNode()

	@classmethod
	def initialize(cls):
		pass


# Initialize the plugin with MObject 
def initializePlugin(plugin):

	vendor = "Adam Fatka - adam.fatka@gmail.com"
	version = "1.0.0"

	plugin_fn = om.MFnPlugin(plugin, vendor, version)

	try:
		plugin_fn.registerNode(HelloWorldNode.TYPE_NAME, 
								HelloWorldNode.TYPE_ID, 
								HelloWorldNode.creator,
								HelloWorldNode.initialize, 
								om.MPxNode.kLocatorNode)
	except:
		om.MGlobal.displayError("Failed to register node: {}".format(HelloWorldNode.TYPE_NAME))

def uninitializePlugin(plugin):
	
	plugin_fn = om.MFnPlugin(plugin)
	try:
		plugin_fn.deregisterNode(HelloWorldNode.TYPE_ID)
	except:
		om.MGlobal.displayError("Failed to deregister Node: {}".format(HelloWorldNode.TYPE_NAME))
		

# if __name__ == "__main__":
# 	plugin_name = "empty_plugin.py"

# 	cmds.evalDeferred("If cmds.pluginInfo('{0}', query = True, loaded = True): cmds.unloadPlugin('{0}')".format(plugin_name)
# 	cmds.evalDeferred("If not cmds.pluginInfo('{0}', query = True, loaded = True): cmds.loadPlugin('{0}')".format(plugin_name)