######################################################################
# main.py
# This is the project file we are going to send CHI
# Only put non-experimentative code in here that we plan on turning in
######################################################################

import PhotoScan

# compatibility check
compatible_major_version = "1.4"
found_major_version = ".".join(PhotoScan.app.version.split('.')[:2])
if found_major_version != compatible_major_version:
	print("PhotoScan version 1.4 is reccomended")

# select region to mask

# find polar coordinates of selected region

# convert polar coordinates to cartesian coordinates

# calculate size of box

# resize bounding area to be slightly larger than the coordinates

# build the denst cloud

# build the mesh

# save?