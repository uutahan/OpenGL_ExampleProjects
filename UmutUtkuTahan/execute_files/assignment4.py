#!/usr/bin/env python3

#CENG487 Assignment3 by
#Umut Utku Tahan
#250201086
#November 2019


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


from camera import Camera
from dividableObject import DividableObject
from scene import Scene

firstMouse=False
lineVision=True
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

my_obj=DividableObject(filename) #instantiate obj with the filename from terminal

grid=Grid()
scene=Scene()
scene.addObject(my_obj)
scene.addObject(grid)

camera=Camera(Vec3d(0,0,8),Vec3d(0,0,-1))

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

# The main drawing function. 
def DrawGLScene():
    global lineVision
    global objVision
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()     # Reset The View 
    gluLookAt(camera.get_view_matrix()[0].x,camera.get_view_matrix()[0].y,camera.get_view_matrix()[0].z,
              camera.get_view_matrix()[1].x,camera.get_view_matrix()[1].y,camera.get_view_matrix()[1].z,
              camera.get_view_matrix()[2].x,camera.get_view_matrix()[2].y,camera.get_view_matrix()[2].z
              )

   
    for obj in scene.objects:
        obj.draw(lineVision,objVision)
       
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
    if(firstMouse):
     
        xoffset=xpos-lastX
        yoffset=ypos-lastY
        
        if abs(xoffset)>abs(yoffset):
            camera.rotate_y(scene.objects[0].get_center(scene.objects[0].points),xoffset/-100)
        else: 
            camera.rotate_x(scene.objects[0].get_center(scene.objects[0].points),yoffset/-100)


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
        camera.move_forward(.1)
    elif args[0] == b"s":
        camera.move_backward(.1)
        
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
        camera=Camera(Vec3d(0,0,8),Vec3d(0,0,-1))

        
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
print("left mouse click :- You can rotate the camera around center of object.")
print("w :- to get closer to object")
print("s :- to get far away from object")
print("f :- to reset the camera position")

print()
print("---ROTATIONS---")
print("z :- to rotate object around its center and z axis.")
print("x :- to rotate object around its center and x axis.")
print("c :- to rotate object around its center and y axis")
print()

print("---CHANGE SUBDIVISION---")
print("b :- to increase subdivision level")
print("n :- to decrease subdivision level")

print()
print("---VISION TYPE---")
print("l :- only line vision active")
print("o :- only object vision active")
print("p :- both line and object vision active(default)")

print()
print("ESC :- quit.")


main()
    