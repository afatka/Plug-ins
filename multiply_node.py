# Simple Math Node

import maya.api.OpenMaya as om 

import maya.cmds as cmds

def maya_useNewAPI():
	pass

class MultiplyNode(om.MPxNode):

	TYPE_NAME = "multiplynode"
	TYPE_ID = om.MTypeId(0x0007f7f8)

	multiplier_obj = None
	multiplicand_obj = None
	product_obj = None

	def __init__(self):
		super(MultiplyNode, self).__init__()

	def compute(self, plug, data): #MPlug object MDataBlock object

		if plug == MultiplyNode.product_obj:

			multiplier = data.inputValue(MultiplyNode.multiplier_obj).asInt() # Read value of mul attr // get data handle >> Get value
			multiplicand = data.inputValue(MultiplyNode.multiplicand_obj).asDouble() # Read value of mulc attr // get data handle >> get value
			product = multiplier * multiplicand # do the math

			product_data_handle = data.outputValue(MultiplyNode.product_obj) # get the product attr data handle
			product_data_handle.setDouble(product) #set the value of the attr

			data.setClean(plug) #set the node's dirty bit to clean

	@classmethod
	def creator(cls):
		return MultiplyNode()

	@classmethod
	def initialize(cls):
		numeric_attr = om.MFnNumericAttribute()

		# create attributes
		cls.multiplier_obj = numeric_attr.create("multiplier", "mul", om.MFnNumericData.kInt, 2) # long name, short name, data type, default value
		numeric_attr.keyable = True # makes the attr visible in the channel box and as an input
		numeric_attr.readable = False # set attr to "write only"

		cls.multiplicand_obj = numeric_attr.create("multiplicand", "mulc", om.MFnNumericData.kDouble, 0.0)
		numeric_attr.keyable = True # makes the attr visible in the channel box and as an input
		numeric_attr.readable = False # set attr to "write only"		

		cls.product_obj = numeric_attr.create("product", "prod", om.MFnNumericData.kDouble, 0.0)
		numeric_attr.writable = False # set attr to "read only"

		# add attributes to the node
		cls.addAttribute(cls.multiplier_obj)
		cls.addAttribute(cls.multiplicand_obj)
		cls.addAttribute(cls.product_obj)

		# Connect output attributes
		cls.attributeAffects(cls.multiplier_obj, cls.product_obj)
		cls.attributeAffects(cls.multiplicand_obj, cls.product_obj)



def initializePlugin(plugin):

	vendor = "Adam Fatka - adam.fatka@gmail.com"
	version = "1.0.0"

	plugin_fn = om.MFnPlugin(plugin, vendor, version)

	try:
		plugin_fn.registerNode(MultiplyNode.TYPE_NAME,  #Node name
							   MultiplyNode.TYPE_ID,    #Node ID
							   MultiplyNode.creator,	#Node creator function
							   MultiplyNode.initialize, #Node initialize function
							   om.MPxNode.kDependNode)  #Type of node - Maya constant
	except Exception as e:
		om.MGlobal.displayError("Failed to register node: {0}".format(MultiplyNode.TYPE_NAME))
		print(e)

def uninitializePlugin(plugin):
	plugin_fn = om.MFnPlugin(plugin)

	try:
		plugin_fn.deregisterNode(MultiplyNode.TYPE_ID)
	except Exception as e:
		om.MGlobal.displayError("Failed to deregister node: {0}".format(MultiplyNode.TYPE_NAME))
		print(e)


if __name__ == "__main__":
	'''
	For development only
	'''

	#clear the scene to unload the plugin
	print("\n\n\n")
	cmds.file(new = True, force = True)

	# Reload the plugin
	plugin_name = "multiply_node.py"

	cmds.evalDeferred("if cmds.pluginInfo('{0}', query = True, loaded = True): cmds.unloadPlugin('{0}')".format(plugin_name))
	cmds.evalDeferred("if not cmds.pluginInfo('{0}', query = True, loaded = True): cmds.loadPlugin('{0}')".format(plugin_name))

	# setup code / testing
	cmds.evalDeferred('cmds.createNode("multiplynode")')