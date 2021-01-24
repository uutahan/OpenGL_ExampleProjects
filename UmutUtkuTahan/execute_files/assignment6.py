#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import shaders
import numpy as np

import sys
sys.path.append("..")

#from box import Box
from box2 import Box
from scene import Scene

box1=Box(.5,.5,.5)
box1.translate(0.55,0,0)

box2=Box(.5,.5,.5)
box2.translate(-0.55,0,0)

scene=Scene()
scene.addObject(box1)
scene.addObject(box2)


lineVision=True
objVision=True

ESCAPE = b'\033'


def render():
    global box1
    global lineVision
    global objVision
    
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
    
    glEnable(GL_DEPTH_TEST)


#    initliaze(box1)
#    drawLines(box1)
#    box1.draw(True,True)
    for i in range(len(scene.objects)):
        
        #draw each object on the scene
        scene.objects[i].draw(lineVision,objVision)
        
        
        s = "Subdivision level is "  #print subdivision level on screen
        s=s+str(scene.objects[i].subdivision_level)
        glColor3f(0.0, 1.0, 0.0)
        #glPushMatrix()
        
        if i==1:
            glWindowPos2d(0,3)
        if i==0:
            glWindowPos2d(458,3)
        for ch in s :
                
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int(ord(ch)))    
      
    
    glutSwapBuffers()
 
    
    
def keyPressed(*args):
    global lineVision
    global objVision
    
    if args[0]==ESCAPE:
        sys.exit()
    
    elif args[0] == b'z':
        scene.objects[0].rotate_point_z(10,scene.objects[0].center)
    elif args[0] == b"x":
        scene.objects[0].rotate_point_x(10,scene.objects[0].center)
    elif args[0] == b"c":
        scene.objects[0].rotate_point_y(10,scene.objects[0].center)
        
    elif args[0] == b'1':
        scene.objects[1].rotate_point_z(10,scene.objects[1].center)
    elif args[0] == b"2":
        scene.objects[1].rotate_point_x(10,scene.objects[1].center)
    elif args[0] == b"3":
        scene.objects[1].rotate_point_y(10,scene.objects[1].center)    
    
        
    elif args[0] == b"b":
        scene.objects[0].increase_subdivisions()
    elif args[0] == b"n":
        scene.objects[0].decrease_subdivisions()
        
    elif args[0] == b"5":
        scene.objects[1].increase_subdivisions()
    elif args[0] == b"6":
        scene.objects[1].decrease_subdivisions()
        
        
    elif args[0] == b"l":
        lineVision=True
        objVision=False
    elif args[0] == b"o":
        lineVision=False
        objVision=True
    elif args[0] == b"p":
        lineVision=True
        objVision=True

        
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

window=0
def main():
    global window
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("CENG487 Homework")
    
    

#    initliaze(box1)
#    drawLines(box1)
    
    glutDisplayFunc(render)
    glutIdleFunc(render)
    
#    glutMouseFunc(mouseEvent)
#    glutMotionFunc(mouseMotion)
    
    glutKeyboardFunc(keyPressed)
    
    InitGL(640, 480)
    glutMainLoop()
    
    

# Print message to console, and kick off the main to get it rolling.
print()
print("   ******* USER GUIDE *******")
print()

print()
print("-----ROTATIONS-----")
print()
print("-BOX ON THE RIGHT")
print("z :- to rotate object around its center and z axis.")
print("x :- to rotate object around its center and x axis.")
print("c :- to rotate object around its center and y axis")
print("-BOX ON THE LEFT")
print("1 :- to rotate object around its center and z axis.")
print("2 :- to rotate object around its center and x axis.")
print("3 :- to rotate object around its center and y axis")
print()

print("-----CHANGE SUBDIVISION-----")
print()
print("-BOX ON THE RIGHT")
print("b :- to increase subdivision level of Box on the right.")
print("n :- to decrease subdivision level of Box on the right.")
print("-BOX ON THE LEFT")
print("5 :- to increase subdivision level of Box on the left.")
print("6 :- to decrease subdivision level of Box on the left.")

print()
print("---VISION TYPE---")
print("l :- only line vision active")
print("o :- only object vision active")
print("p :- both line and object vision active(default)")

print()
print("Dividing surface and then making rotations doesnt break behaviour")

print()
print("ESC :- quit.")

main()