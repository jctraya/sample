from SimpleCV import Camera, Display
#global x
def main():

    x = 0;
    cam  = Camera (prop_set={'width':640, 'height':480})
    disp = Display (resolution=(320,240))
    while disp.isNotDone():
        img = cam.getImage()
        img = img.scale(0.5)
        faces = img.findHaarFeatures("eye.xml")
        #print "not Detected"
        if faces:
            for face in faces:
                face.draw()
                print "eyes Detected"
               # x = 0
        else:
            
                 # x += 1

                 print "close eyes"
                  #print (x)    
                  #if x > 10:
                  #  print "HOY GISING"

                   # return main()
        img.save(disp)

        

 #if x > 15:
 #print("Hoy gising")

if __name__ == "__main__":
    main()
