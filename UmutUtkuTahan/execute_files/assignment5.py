#!/usr/bin/env python3

#CENG487 Assignment5 by
#Umut Utku Tahan
#250201086
#December 2019


# Note:
# -----
# This Uses PyOpenGL and PyOpenGL_accelerate packages.  It also uses GLUT for UI.
# To get proper GLUT support on linux don't forget to install python-opengl package using apt
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys
sys.path.append("..")

from vec3d import Vec3d
from grid import Grid

from cornellBox import CornellBox
from objParser2 import ObjParser2

from camera import Camera
from scene import Scene


from material import Material
from light import Light



firstMouse=False
lineVision=False
objVision=True

if(len(sys.argv)<2):
    print("Please input .obj file to command line (its either tori.obj or ecube.obj)")
    sys.exit()
if(len(sys.argv)>2):
    print("input only one .obj file to command line")
    sys.exit()

filename=sys.argv[1] #get the filename from terminal

if filename.split(".")[1] !="obj":  # if file type is not .obj print error message and exit
    print("please input .obj file type to command line")
    sys.exit()
    
   


parser=ObjParser2(filename)
cornellObjectPoints=parser.objects
cornellObjects=[]
for points in cornellObjectPoints:
    cornellObjects.append(CornellBox(points))


cornellObjects[0].setRgbColor([0.96,0.85,0.69]) #short box
cornellObjects[1].setRgbColor([0.96,0.85,0.69]) #tall box
cornellObjects[2].setRgbColor([0.96,0.85,0.69]) #floor
cornellObjects[3].setRgbColor([0.96,0.85,0.69]) #ceiling
cornellObjects[4].setRgbColor([1,0,0]) #left wall
cornellObjects[5].setRgbColor([0,1,0])#right wall
cornellObjects[6].setRgbColor([0.96,0.85,0.69]) #back wall

cornellObjects[0].setMaterial(Material([1,1,1,1],[0.1,0.1,0.2,1],0))
cornellObjects[1].setMaterial(Material([1,1,1,1],[0.1,0.1,0.1,1],127))
cornellObjects[2].setMaterial(Material([1,1,1,1],[0.3,0.1,0.1,1],127))
cornellObjects[3].setMaterial(Material([1,1,1,1],[0.1,0.1,0.1,1],127))
cornellObjects[4].setMaterial(Material([1,1,1,1],[0.2,0.2,0.1,1],127))
cornellObjects[5].setMaterial(Material([1,1,1,1],[0.3,0.1,0.1,1],127))
cornellObjects[6].setMaterial(Material([1,1,1,1],[0.1,0.2,0.1,1],127))

   

grid=Grid()
scene=Scene()
for obj in cornellObjects:
    scene.addObject(obj)
#scene.addObject(grid)

camera=Camera(Vec3d(-3,25,76),Vec3d(0,0,-1))




light1=Light([ 0.6,0.6,0.6, 1 ], [ 1,1,1, 1 ], [ .1,.1,.1, 1 ],[16,44,0,1] ,1) 
light2=Light([ 0.6,0.6,0.6, 1 ], [ 1,1,1, 1 ], [ .1,.1,.1, 1 ],[-3.4,25,90] ,2) #you can detect light2 by pressing s and going backward from initial position
light2.switchLight() #turning of the light2.

scene.addObject(light1)
scene.addObject(light2)






# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\033'

# Number of the glut window.
window = 0
# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):              # We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black
    glClearDepth(1.0)                   # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
    glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    # Reset The Projection Matrix
                                        # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
          

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:                     # Prevent A Divide By Zero If The Window Is Too Small 
        Height = 1

    glViewport(0, 0, Width, Height)     # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

rotationFlag=False

# The main drawing function. 
def DrawGLScene():
    global rotationFlag
    global lineVision
    global objVision
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()     # Reset The View 
    gluLookAt(camera.get_view_matrix()[0].x,camera.get_view_matrix()[0].y,camera.get_view_matrix()[0].z,
              camera.get_view_matrix()[1].x,camera.get_view_matrix()[1].y,camera.get_view_matrix()[1].z,
              camera.get_view_matrix()[2].x,camera.get_view_matrix()[2].y,camera.get_view_matrix()[2].z
              )

    #glShadeModel(GL_SMOOTH)
    #glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
    glEnable(GL_LIGHTING)
    glEnable(GL_NORMALIZE)
 
    for obj in scene.objects:
        obj.draw(lineVision,objVision)
        
    if rotationFlag==True:
        for i in range(1000000):
            if i==2:
                light1.changePos()
        
    #  since this is double buffered, swap the buffers to display what just got drawn. 
    glutSwapBuffers()


lastX=320
lastY=240
def mouseEvent(button,state,xpos,ypos):
    global firstMouse
    global lastX
    global lastY
    if (button == GLUT_LEFT_BUTTON) and (state == GLUT_DOWN):
        firstMouse=True

        lastX=xpos
        lastY=ypos
        
    else:
        firstMouse=False
        
def mouseMotion(xpos,ypos):
    global firstMouse
    global lastX
    global lastY
    if(firstMouse):
     
        xoffset=xpos-lastX
        yoffset=ypos-lastY
        
        
        camera.updateYawPitch(xoffset,-yoffset)
        camera.updateFrontFromYawPitch()
        
#        if abs(xoffset)>abs(yoffset):
#            camera.rotate_y(scene.objects[0].get_center(scene.objects[0].points),xoffset/-100)
#            
#        else: 
#            camera.rotate_x(scene.objects[0].get_center(scene.objects[0].points),yoffset/-100)


def keyPressed(*args):
    
    global camera
    global lineVision
    global objVision
    
    key=glutGetModifiers()
    
    #print(args[0])
    
    # If escape is pressed, kill everything.
    if args[0]==ESCAPE:
        sys.exit()
    elif args[0] == b'z':
        scene.objects[0].rotate_point_z(10,scene.objects[0].center)
    elif args[0] == b"x":
        scene.objects[0].rotate_point_x(10,scene.objects[0].center)
    elif args[0] == b"c":
        scene.objects[0].rotate_point_y(10,scene.objects[0].center)
        
    elif args[0] == b"b":
        scene.objects[0].increase_subdivisions()
    elif args[0] == b"n":
        scene.objects[0].decrease_subdivisions()

 
        
    elif args[0] == b"w":
        camera.move_forward(1)
    elif args[0] == b"s":
        camera.move_backward(1)
    elif args[0] == b"a":
        camera.move_left(1)
    elif args[0] == b"d":
        camera.move_right(1)
        
    elif args[0] == b"l":
        lineVision=True
        objVision=False
    elif args[0] == b"o":
        lineVision=False
        objVision=True
    elif args[0] == b"p":
        lineVision=True
        objVision=True
        
    elif args[0] == b"f":
        camera=Camera(Vec3d(-3.5,25,76),Vec3d(0,0,-1))
        
    elif args[0] == b"u":
        light1.changePos()
    elif args[0] == b"i":
        global rotationFlag
        rotationFlag=not rotationFlag
    elif args[0] == b"y":
        light1.switchLight()

        
def main():
    glutInit(sys.argv)
    
    
    # Select type of Display mode:   
    #  Double buffer 
    #  RGBA color
    # Alpha components supported 
    # Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("CENG487 Homework")

    # Display Func
    glutDisplayFunc(DrawGLScene)

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
    
    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(keyPressed)
    
    glutMouseFunc(mouseEvent)
    glutMotionFunc(mouseMotion)

    # Initialize our window. 
    InitGL(640, 480)
    

    # Start Event Processing Engine 
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print()
print("   ******* USER GUIDE *******")
print()

print("---CAMERA CONTROLS---")
print("left mouse click :- change where you are looking")
print("w :- to move forward")
print("s :- to move backward")
print("a :- to move left")
print("d :- to move right")
print("f :- to reset the camera position")

print()
print("---LIGHT---")
print("There is second light in screen but its off, you can notice it by going backward from start")
print("y :- to switch lighting on and off.")
print("u :- to rotate light object when holding to key u.")
print("i :- to rotate light object continuously(if pressed again object stops)")
print()

print()
print("---VISION TYPE---")
print("l :- only line vision active")
print("o :- only object vision active(default)")
print("p :- both line and object vision active")

print()
print("ESC :- quit.")


main()
    