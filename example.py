def test(imX,imY):
	doc = PhotoScan.app.document
	chunk = doc.chunk
	camera = chunk.cameras[0]
	point2D = PhotoScan.Vector([imX, imY])
	print (point2D)
	sensor = camera.sensor
#	v = chunk.model.pickPoint(camera.center, camera.transform.mulp(sensor.calibration.unproject(point2D)))
	v = chunk.point_cloud.pickPoint(camera.center, camera.transform.mulp(sensor.calibration.unproject(point2D)))
	v_t = chunk.transform.matrix.mulp(v)
	v_t.size = 3
	v_out_world = chunk.crs.project(v_t)
	print(v_out_world)

# 	v_unproj = chunk.crs.unproject(v_proj)
	v_unproj = chunk.crs.unproject(v_out_world)
	v_inv = chunk.transform.matrix.inv().mulp(v_unproj)
	v_inv.size = 3
	v_out_pix = sensor.calibration.project(camera.transform.inv().mulp(v_inv))
	print(v_out_pix)