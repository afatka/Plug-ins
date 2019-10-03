# Maya API 2.0 Plug-in Template

import maya.api.OpenMaya as om
import maya.cmds as cmds

# Inform Maya to use API 2.0
def maya_useNewAPI():
	pass

# maya_useNewApi = True

class HelloWorldCmd(om.MPxCommand):
	
	COMMAND_NAME = "HelloWorld"

	def __init__(self):
		super(HelloWorldCmd, self).__init__()

	def doIt(self, args):
		print("Hello World")

	@classmethod
	def creator(cls):
		return HelloWorldCmd()


# Initialize the plugin with MObject 
def initializePlugin(plugin):
	"""
	"""

	vendor = "Adam Fatka - adam.fatka@gmail.com"
	version = "1.0.0"

	plugin_fn = om.MFnPlugin(plugin, vendor, version)
	try:
		plugin_fn.registerCommand(HelloWorldCmd.COMMAND_NAME, HelloWorldCmd.creator)
	except:
		om.MGlobal.displayError("Failed to register command: {}".format(HelloWorldCmd))

def uninitializePlugin(plugin):
	"""
	"""
	plugin_fn = om.MFnPlugin(plugin)
	try:
		plugin_fn.deregisterCommand(HelloWorldCmd.COMMAND_NAME)
	except:
		om.MGlobal.displayError("Failed to deregisterCommand: {}".format(HelloWorldCmd))

# if __name__ == "__main__":
# 	plugin_name = "hello_world.py"

# 	cmds.evalDeferred("If cmds.pluginInfo('{0}', query = True, loaded = True): cmds.unloadPlugin('{0}')".format(plugin_name)
# 	cmds.evalDeferred("If not cmds.pluginInfo('{0}', query = True, loaded = True): cmds.loadPlugin('{0}')".format(plugin_name)