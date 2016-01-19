from SimpleCV import Camera, Display
from time import sleep

myCamera = Camera (prop_set={'width':640, 'height':480})

myDisplay = Display(resolution=(640,480))

while not myDisplay.isDone():
	frame = myCamera.getImage()
	frame = frame.scale(0.5)
	faces = frame.findHaarFeatures("face.xml")
	
    faces = faces.sortArea() 
    faces = faces[-1] #picking the largest face
    faces = img.crop(faces) #crops face from the image

	if faces:
		for face in faces:
			face.draw()

	else:
		print "No Faces detected."

		

	frame.save(myDisplay)
	sleep(.1)
