import maya.api.OpenMaya as om 

import maya.cmds as cmds

def maya_useNewAPI():
	pass

class RollingNode(om.MPxNode):

	TYPE_NAME = "rollingnode" # node type name
	TYPE_ID = om.MTypeId(0x0007f79) # unique identifier

	#declare class variables
	distance_obj = None # MObject for distance
	radius_obj = None # MObject for radius
	rotation_obj = None # MObject for rotation

	def __init__(self):
		super(RollingNode, self).__init__()

	def compute(self, plug, data):
		
		if plug == self.rotation_obj: # verify that the plug is for the correct attr

			# get distance and radius values from the data block
			distance = data.inputValue(RollingNode.distance_obj).asDouble()
			radius = data.inputValue(RollingNode.radius_obj).asDouble()

			if radius == 0:
				rotation = 0
			else:
				# calculate the rotation
				rotation = distance / radius

			# get the data handle to the output attribute
			rotation_data_handle = data.outputValue(RollingNode.rotation_obj)
			# set the value
			rotation_data_handle.setDouble(rotation)

			# set node as "clean"
			data.setClean(plug)

	@classmethod
	def creator(cls):
		return RollingNode()

	@classmethod
	def initialize(cls):
		numeric_attr = om.MFnNumericAttribute()

		# create distance attr for node (hide the output and make it show in the channel box)
		cls.distance_obj = numeric_attr.create("distance", "dist", om.MFnNumericData.kDouble, 0.0)
		numeric_attr.readable = False
		numeric_attr.keyable = True

		# create radius attr for node (hide the output and make it show in the channel box)
		cls.radius_obj = numeric_attr.create("radius", "rad", om.MFnNumericData.kDouble, 0.0)
		numeric_attr.readable = False
		numeric_attr.keyable = True

		unit_attr = om.MFnUnitAttribute()

		# create the rotation atter as type(MAngle)
		cls.rotation_obj = unit_attr.create("rotation", "rot", om.MFnUnitAttribute.kAngle, 0.0)

		# add the attrs to the node
		cls.addAttribute(cls.distance_obj)
		cls.addAttribute(cls.radius_obj)
		cls.addAttribute(cls.rotation_obj)

		# Connect input and output attr relationships
		cls.attributeAffects(cls.distance_obj, cls.rotation_obj)
		cls.attributeAffects(cls.radius_obj, cls.rotation_obj)




def initializePlugin(plugin):

	vendor = "Adam Fatka adam.fatka@gmail.com"
	version = "1.0.0"

	plugin_fn = om.MFnPlugin(plugin, vendor, version)

	try:
		plugin_fn.registerNode(RollingNode.TYPE_NAME,
							   RollingNode.TYPE_ID, 
							   RollingNode.creator,
							   RollingNode.initialize,
							   om.MPxNode.kDependNode)
	except Exception as e:
		om.MGlobal.displayError("Failed to register node: {0}\n{1}".format(RollingNode.TYPE_NAME, e))

def uninitializePlugin(plugin):

	plugin_fn = om.MFnPlugin(plugin)

	try:
		plugin_fn.deregisterNode(RollingNode.TYPE_ID)
	except Exception as e:
		om.MGlobal.displayError("Failed to deregister node: {0}\n{1}".format(RollingNode.TYPE_NAME, e))


if __name__ == "__main__":
	'''
	For development only
	'''

	#clear the scene to unload the plugin
	print("\n\n\n")
	cmds.file(new = True, force = True)

	# Reload the plugin
	plugin_name = "rolling_node.py"

	cmds.evalDeferred("if cmds.pluginInfo('{0}', query = True, loaded = True): cmds.unloadPlugin('{0}')".format(plugin_name))
	cmds.evalDeferred("if not cmds.pluginInfo('{0}', query = True, loaded = True): cmds.loadPlugin('{0}')".format(plugin_name))

	# setup code / testing
	# cmds.evalDeferred('cmds.createNode("rollingnode")')

	cmds.evalDeferred('cmds.file("/Users/afatka/Desktop/rolling.ma", open = True, force = True)')