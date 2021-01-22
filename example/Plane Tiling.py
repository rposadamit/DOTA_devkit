import os

# We define 2 types of tile.
# Type 1: The ones made by splitting in the natural way from the top-left corner. Equivalent to tiling a floor.
# Type 2: Tiles that are not type 1. We will use these in case there is a plane chopped in the original type 1 tiling.
# the following function first tries to find a Type 1 tile that includes the whole plane, if not possible, it returns a
# Type 2 that does. It returns the top-left corner of a tile, and as a 3rd argument it returns the new values 
# of the quadrilateral boundary indexed as part of the tile, not of the bigger image.
def find_tile(plane):
	'''
	INPUT: 
	plane: a string that gives a plane's quadrilateral boundary, in the DOTA format
	OUTPUT:
	tuple: If the quadrilateral boundary is within a type 1 tile, return the top-left corner of that tile;
		else, return the type 2 tile that contains the such plane
	'''
	lst = plane.split()
	corners = [(int(lst[0]),int(lst[1])), (int(lst[2]),int(lst[3])), (int(lst[4]),int(lst[5])), (int(lst[6]),int(lst[7]))]
	tile = set(), set() # we will see if there is EXACTLY ONE type 1 tile that contains all the corners
	min_r, min_c = None, None 
	for c in corners:
		tile[0].add(c[0]//512)
		tile[1].add(c[1]//512)
		if min_r==None or c[0]<min_r:
			min_r = c[0]
		if min_c == None or c[1]<min_c:
			min_c = c[1]
	if len(tile[0])==1:
		if len(tile[1])==1:
			# if there is exactly one, we return the coordinates of its top-left corner
			i = tile[0].pop()
			j = tile[1].pop()
			return (i*512, j*512, [ (r-i*512, c- j*512) for (r,c) in corners])
	# if there is more than one, we return the top-left corner of the bottom-right-most tile that holds the four corners
	return (min_r, min_c, [ (r-min_r*512, c- min_c*512) for (r,c) in corners])

# retrieve the list of images with planes
plane_images = 'C:\\Users\\rodri\\Documents\\Github\\DOTA_devkit\\example\\plane_images.text'
d = open(plane_images, 'r' ,encoding="Latin-1")
# notice that objects is a txt file, not an image
for address in d.readlines():
	txt = open(address)
	planes = []
	# in the txt file, we filter the objects that are planes
	for line in txt.readlines():
		if "plane" in line:
			planes.append(line.strip('\n'))

	# Now with all the planes separated, we build the set of tiles that hold the planes. 
	tiles = dict()
	for plane in planes:
		r,c, quad_bound = find_tile(plane)
		try:
			tiles[(r,c)].add((plane, quad_bound))
		except:
			tiles[(r,c)] = [(plane,quad_bound)]
