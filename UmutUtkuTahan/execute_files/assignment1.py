#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#October 2019


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
from camera import Camera
from scene import Scene
from rectangle2d import Rectangle2d
from triangle2d import Triangle2d

lineVision=True
objVision=True

scene=Scene()

rec=Rectangle2d(1,1)
tri=Triangle2d(1.15)
tri.translate(0,-0.5,0)

scene.addObject(rec)
scene.addObject(tri)



camera=Camera(Vec3d(1,0,5),Vec3d(0,0,-1))
# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\033'

# Number of the glut window.
window = 0

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small 
	    Height = 1

    glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
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
    glLoadIdentity()					# Reset The View 
    gluLookAt(camera.get_view_matrix()[0].x,camera.get_view_matrix()[0].y,camera.get_view_matrix()[0].z,
              camera.get_view_matrix()[1].x,camera.get_view_matrix()[1].y,camera.get_view_matrix()[1].z,
              camera.get_view_matrix()[2].x,camera.get_view_matrix()[2].y,camera.get_view_matrix()[2].z
              )

    for obj in scene.objects:
        obj.draw(lineVision,objVision)
        glTranslatef(2.0, 0.0, 0.0)
    
	# Move Left 1.5 units and into the screen 6.0 units.
	#glTranslatef(-1.5, 0.0, -6.0)

    
    
    glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
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
        scene.objects[0].rotate_point_z(10,scene.objects[0].getTopLeft())
    elif args[0] == b"c":
        scene.objects[0].rotate_point_z(10,scene.objects[0].getTopRight())
        
    elif args[0] == b'1':
        scene.objects[1].rotate_point_z(10,scene.objects[1].center)
    elif args[0] == b"2":
        scene.objects[1].rotate_point_z(10,scene.objects[1].getBottomRight())
    elif args[0] == b"3":
        scene.objects[1].rotate_point_z(10,scene.objects[1].getBottomLeft())
        
    elif args[0] == b"b":
        scene.objects[0].increase_subdivisions()
    elif args[0] == b"n":
        scene.objects[0].decrease_subdivisions()
    
    elif args[0] == b"5":
        scene.objects[1].increase_subdivisions()
    elif args[0] == b"6":
        scene.objects[1].decrease_subdivisions()

 
        
    elif args[0] == b"w":
        camera.move_forward(.1)
    elif args[0] == b"s":
        camera.move_backward(.1)
    elif args[0] == b"a":
        camera.move_left(.1)
    elif args[0] == b"d":
        camera.move_right(.1)
        
        
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
        camera=Camera(Vec3d(1,0,5),Vec3d(0,0,-1))     
def main():
    
    global window
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

	# Initialize our window. 
    InitGL(640, 480)
    

	# Start Event Processing Engine	
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print()
print("   ******* USER GUIDE *******")
print()

print("---CAMERA CONTROLS---")
print("w :- to move forward")
print("s :- to move backward")
print("a :- to move left")
print("d :- to move right")
print("f :- to reset the camera position")

print()
print("-----ROTATIONS-----")
print()
print("-SQUARE")
print("z :- to rotate rectangle around its center.")
print("x :- to rotate rectangle around its top left corner.")
print("c :- to rotate rectangle around its top right corner")
print("-TRIANGLE")
print("1 :- to rotate triangle around its center.")
print("2 :- to rotate triangle around its bottom right corner.")
print("3 :- to rotate triangle around its bottom left corner")
print()

print("-----CHANGE SUBDIVISION-----")
print()
print("-SQUARE")
print("b :- to increase subdivision level of Rectangle.")
print("n :- to decrease subdivision level of Rectangle.")
print("-TRIANGLE")
print("5 :- to increase subdivision level of Triangle.")
print("6 :- to decrease subdivision level of Triangle.")

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
#print(triangle.points)
    