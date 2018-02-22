import PhotoScan, math

doc = PhotoScan.app.document
chunk = doc.chunk
region = chunk.region
T = chunk.transform.matrix

# initializing vector with coordinates
m = PhotoScan.Vector([10E+10, 10E+10, 10E+10])
M = -m

# calculate the bounds based on "valid" points
for point in chunk.point_cloud.points:
	if not point.valid:
		continue
	coord = T * point.coord	
	coord.size = 3
	coord = chunk.crs.project(coord)
	for i in range(3):
		m[i] = min(m[i], coord[i])
		M[i] = max(M[i], coord[i])
		
center = (M + m) / 2
size = M - m

# resize vector
region.center = T.inv().mulp(chunk.crs.unproject(center))
region.size = size * (1 / T.scale())

# 3d model creation
v_t = T * PhotoScan.Vector( [0,0,0,1] )
v_t.size = 3
R = chunk.crs.localframe(v_t) * T
region.rot = R.rotation().t()

chunk.region = region
print("Script finished.")

