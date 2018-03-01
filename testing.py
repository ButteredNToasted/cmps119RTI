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


#	chunk.point_cloud()
	chunk.optimizeCameras(fit_f = True, fit_cx = True, fit_cy = True, fit_b1 = True, fit_b2 = True, fit_k1 = True, fit_k2 = True, fit_k3 = True, fit_k4 = True, fit_p1 = True, fit_p2 = True, fit_p3 = True, fit_p4 = True)
	#optimize camera alignment
	chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, generic_preselection=True, reference_preselection = False)
	chunk.alignCameras()

	xmin = 10E+10
	ymin = 10E+10
	zmin = 10E+10
	xmax = -xmin
	ymax = -ymin
	zmax = -zmin
	padding = 1 + 0.05		#Padding = Original size + Buffer %
#	source = shapes.crs
#	out = PhotoScan.CoordinateSystem("EPSG::3948")
	for shape in chunk.shapes:
#		shape.vertices = [PhotoScan.CoordinateSystem.transform(v, source, out) for v in shape.vertices]

		print(shape.vertices)
		  
		#creates an array to hold all of the vertices for the shapes 
		verts = [[] for _ in range(len(shape.vertices))] 
		a = 0
		for v in shape.vertices:
#			print(v.size)
			
			b = 3
			ver = [[] for _ in range(b)]
			ver = [[v.x],[v.y],[v.z]]

			if v.x > xmax:
				xmax = v.x
			if v.x < xmin:
				xmin = v.x

			if v.y > ymax:
				ymax = v.y
			if v.y < ymin:
				ymin = v.y

			if v.z > zmax:
				zmax = v.z
			if v.z < zmin:
				zmin = v.z
				#places the vertice in the array holding all of the vertices 
				verts[a] = ver
				a = a + 1
#				print(v)
	Maxvert = PhotoScan.Vector([xmax,ymax,zmax])
	Minvert = PhotoScan.Vector([xmin,ymin,zmin])

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

	region.center = Mat.inv().mulp(chunk.crs.unproject(Center))
	region.size = Size*(1/Mat.scale())
	print(region.size)

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
	chunk.buildDepthMaps(quality=PhotoScan.MediumQuality, filter = PhotoScan.AggressiveFiltering)
	
	#build dense cloud
	chunk.buildDenseCloud()
	
	#build mesh
	chunk.buildModel(surface = PhotoScan.Arbitrary, interpolation = PhotoScan.EnabledInterpolation)

	print("Importing masks")
	chunk.importMasks(path = '', source = PhotoScan.MaskSourceModel, operation = PhotoScan.MaskOperationReplacement, tolerance = 10, cameras = chunk.cameras)
	#build texture
#	chunk.buildTexture(blending = PhotoScan.MosaicBlending, size = 4096)
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
