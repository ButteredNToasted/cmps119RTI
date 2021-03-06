# Project description
Automate creation of masks on photos, based on drawing a polygon on a model. 
This one will require some understanding of computer graphics and 3D. The goal is to allow a user to draw a polygon on an area on a built model (could be dense cloud or mesh) and then find all the photos that have that part of the model in them, and mask out that area on the photos. Note that Photoscan has calculated the information about which photos “see” what parts of the model, so this is not required.  However, many photos (6-12 or more) could include an area on any given surface. This includes photos from different distances and different focal lengths, they can even be from different physical cameras with different pixel resolutions. (i.e. the area could be much larger or smaller on individual photos, due to the distance focal length and resolution) Photoscan provides basic tools for making masks.  This would be extremely useful for example with wrought iron gate, or other subject matter that has negative space. The problem is made more challenging by the fact that some images may already have masks, and you would need to detect the existing masks, and add to them where appropriate.

# Usage

Open project in PhotoScan
Import script
Select tools/tie points/build point cloud
	Run on high setting
Run script:
	Custom scripts/Shrink region to shape