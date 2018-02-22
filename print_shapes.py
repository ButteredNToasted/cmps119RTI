import PhotoScan

# Checking compatibility
compatible_major_version = "1.4"
found_major_version = ".".join(PhotoScan.app.version.split('.')[:2])
if found_major_version != compatible_major_version:
	raise Exception("Incompatible PhotoScan version: {} != {}".format(found_major_version, compatible_major_version))


def get_shape_inf():

	chunk = PhotoScan.app.document.chunk
	shapes = chunk.shapes
	#source = shapes.crs
	#out = PhotoScan.CoordinateSystem("EPSG::3948")
	for shape in chunk.shapes:
		#shape.vertices = [PhotoScan.CoordinateSystem.transform(v, source, out) for v in shape.vertices]
		print(shape.vertices)
	#shapes.crs = out

	print("Script finished!")


label = "Custom menu/Read RunThis metadata1"
PhotoScan.app.addMenuItem(label, get_shape_inf)
print("To execute this script press {}".format(label))