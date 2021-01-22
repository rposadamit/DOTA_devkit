import os

# set where to store the filtered images, and open the address
plane_images = 'C:\\Users\\rodri\\Documents\\Github\\DOTA_devkit\\example\\plane_images.text'
d = open(plane_images, 'w+' ,encoding="Latin-1")


# set where are the images to check, and list them all 
raw_dir = 'C:\\Users\\rodri\\Documents\\Github\\DOTA_devkit\\example\\labelTxt'
images = os.listdir(raw_dir)

# for each, check whether they have 'plane'
for path in images:
	f = open(raw_dir+'\\' + path, 'r+', encoding="Latin-1")
	if 'plane' in f.read():
		# if an image does, write the address of the image
		d.write(raw_dir+'\\'+path)
	f.close()
d.close()


