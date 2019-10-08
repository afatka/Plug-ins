import maya.api.OpenMaya as om
import maya.api.OpenMayaRender as omr 
import maya.api.OpenMayaUI as omui 

import maya.cmds as cmds

# Inform Maya to use API 2.0
def maya_useNewAPI():
	pass

class HelloWorldNode(omui.MPxLocatorNode):

	TYPE_NAME = "helloworld"
	TYPE_ID = om.MTypeId(0x0007f7f7)
	DRAW_CLASSIFICATION = "drawdb/geometry/helloworld"
	DRAW_REGISTRANT_ID = "HelloWorldNode"

	def __init__(self):
		super(HelloWorldNode, self).__init__()

	@classmethod
	def creator(cls):
		return HelloWorldNode()

	@classmethod
	def initialize(cls):
		pass

class HelloWorldDrawOverride(omr.MPxDrawOverride):

	NAME = 'HelloWorldDrawOverride'


	def __init__(self, obj):
		super(HelloWorldDrawOverride, self).__init__( obj, None, False)

	def prepareForDraw(self, obj_path, camera_path, frame_context, old_data):
		pass

	def supportedDrawAPIs(self):
		return (omr.MRenderer.kAllDevices)

	def hasUIDrawables(self):
		return True 

	def addUIDrawables(self, obj_path, draw_manager, frame_context, data):
		draw_manager.beginDrawable()

		draw_manager.text2d(om.MPoint(100,100), "Hello World")

		draw_manager.endDrawable()

	@classmethod
	def creator(cls, obj):
		return HelloWorldDrawOverride(obj)

# Initialize the plugin with MObject 
def initializePlugin(plugin):

	vendor = "Adam Fatka - adam.fatka@gmail.com"
	version = "1.0.0"
	api_version = "Any"

	plugin_fn = om.MFnPlugin(plugin, vendor, version, api_version)

	try:
		plugin_fn.registerNode(HelloWorldNode.TYPE_NAME, 
							   HelloWorldNode.TYPE_ID, 
							   HelloWorldNode.creator,
							   HelloWorldNode.initialize, 
							   om.MPxNode.kLocatorNode,
							   HelloWorldNode.DRAW_CLASSIFICATION)
	except:
		om.MGlobal.displayError("Failed to register node: {}".format(HelloWorldNode.TYPE_NAME))

	try:
		omr.MDrawRegistry.registerDrawOverrideCreator(HelloWorldNode.DRAW_CLASSIFICATION, 
													  HelloWorldNode.DRAW_REGISTRANT_ID,
													  HelloWorldDrawOverride.creator)
	except:
		om.MGlobal.displayError("Failed to register draw override: {}".format(HelloWorldDrawOverride.NAME))

def uninitializePlugin(plugin):
	plugin_fn = om.MFnPlugin(plugin)

	try:
		omr.MDrawRegistry.deregisterDrawOverrideCreator(HelloWorldNode.DRAW_CLASSIFICATION, 
													    HelloWorldNode.DRAW_REGISTRANT_ID)
	except:
		om.MGlobal.displayError("Failed to deregister draw override: {}".format(HelloWorldDrawOverride.NAME))
	
	try:
		plugin_fn.deregisterNode(HelloWorldNode.TYPE_ID)
	except:
		om.MGlobal.displayError("Failed to deregister Node: {}".format(HelloWorldNode.TYPE_NAME))
		

if __name__ == "__main__":

    cmds.file(new=True, force=True)

    plugin_name = "hello_world_node.py"

    cmds.evalDeferred('if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(plugin_name))

    cmds.evalDeferred('cmds.createNode("helloworld")')