# This is the project file we are going to send CHI
# Only put non-experimentative code in here that we plan on turning in

import PhotoScan
#import pprint
#import np

# compatibility check
compatible_major_version = "1.4"
found_major_version = ".".join(PhotoScan.app.version.split('.')[:2])
if found_major_version != compatible_major_version:
	print("PhotoScan version 1.4 is reccomended")

# select region to mask
def get_shape_inf():

	chunk = PhotoScan.app.document.chunk
	region = chunk.region
	Mat = chunk.transform.matrix
	shapes = chunk.shapes

	chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, generic_preselection=True, reference_preselection = False)
	chunk.alignCameras()

	xmin = 10E+10
	ymin = 10E+10
	zmin = 10E+10
	xmax = -xmin
	ymax = -ymin
	zmax = -zmin
	padding = 10		#Padding = Original size + Buffer %
#	source = shapes.crs
#	out = PhotoScan.CoordinateSystem("EPSG::3948")
	for shape in chunk.shapes:
#		shape.vertices = [PhotoScan.CoordinateSystem.transform(v, source, out) for v in shape.vertices]

		print(shape.vertices)
		  

		x_vals = []
		y_vals = []
		z_vals = []
		#creates an array to hold all of the vertices for the shapes 
		verts = [[] for _ in range(len(shape.vertices))] 
		a = 0
		for v in shape.vertices:
#			print(v.size)

			x_vals.append(v[0])
			y_vals.append(v[1])
			z_vals.append(v[2])
			

			b = 3
			ver = [[] for _ in range(b)]
			ver = [[v.x],[v.y],[v.z]]
	
	xmax = max(x_vals)
	ymax = max(y_vals)
	zmax = max(z_vals)

	xmin = min(x_vals)
	ymin = min(y_vals)
	zmin = min(z_vals)


	Maxvert = PhotoScan.Vector([xmax,ymax,zmax])
	Minvert = PhotoScan.Vector([xmin,ymin,zmin])

	print("Min/Max vectors:")
	print(Maxvert)
	print(Minvert)

	#Scale
	Maxvert *= padding
	Minvert *= padding	

			#prints all of the vertices for the shapes 		
#	print("verts:")
#	print(verts)
#	print(xmax)
#	print(xmin)
#	print(ymax)
#	print(ymin)
#	print(zmax)
#	print(zmin)
#	print(Maxvert)
#	print(Minvert)
	
	Center = (Maxvert + Minvert)/2		#find center of region
	Size = Maxvert - Minvert		#find size of region

	print("REGION CENTER BEFORE INVERSION")
	print(region.center)
	region.center = Mat.inv().mulp(chunk.crs.unproject(Center))
	region.size = Size*(1/Mat.scale())
	print("REGION CENTER AFTER INVERSION")
	print(region.center)
	#print(region.size)

	region.center.z = region.center.z*-1
	print("REGION CENTER")
	print(region.center)

	v_t = Mat*PhotoScan.Vector([0,0,0,1])
	v_t.size = 3
	R = chunk.crs.localframe(v_t)*Mat
	region.rot = R.rotation().t()
	chunk.region = region

	#shapes.crs = out

	#Match photos
#	chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, generic_preselection=True, reference_preselection = False)
#	chunk.alignCameras()

	#build depth maps
	print("building depth map")
	chunk.buildDepthMaps(quality=PhotoScan.MediumQuality, filter = PhotoScan.AggressiveFiltering)
	
	#build dense cloud
	print("building dense cloud")
	chunk.buildDenseCloud()
	
	#build mesh
	print("building model")
	chunk.buildModel(surface = PhotoScan.Arbitrary, interpolation = PhotoScan.EnabledInterpolation)
	
	#build texture
	print("building texture")
	chunk.buildTexture(blending = PhotoScan.MosaicBlending, size = 4096)
	print("Script finished!")


label = "Custom Scripts/Shrink Region to Shape"
PhotoScan.app.addMenuItem(label, get_shape_inf)
print("To execute this script press {}".format(label))

# find polar coordinates of selected region

# convert polar coordinates to cartesian coordinates

# calculate size of box

# resize bounding area to be slightly larger than the coordinates

# build the denst cloud

# build the mesh

# save
