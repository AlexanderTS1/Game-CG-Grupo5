# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import math
import random as rdn
import numpy as np

### Algorithm ###

def set_pixel(x, y, r, g, b, size):
	glColor3f(r, g, b)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()
	
	# print("{}\t{}".format(x, y))
	# pygame.time.wait(100)

	# option 1 (ok)
	#pygame.display.flip()
	
	# option 2
	glFlush()

def color_pixel(width, height, x, y, size):
	rgb = glReadPixels(width / 2 + x , height / 2 + y, size ,size , 
						GL_RGB, GL_UNSIGNED_BYTE, None)
	return list(rgb)

def clearCanvas():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def Traslate(vertices, tx, ty):
	T = [
		[1, 0, tx], 
		[0, 1, ty], 
		[0, 0, 1]
	]
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	return result

def Scale(vertices, Sx,Sy):
	R = [
		[Sx, 0, 0], 
		[0, Sy, 0],
		[0, 0, 1]
	]
	result = []
	for item in vertices:
		point = np.dot(R, item)
		result.append(point)
	return result

"""def Defender(x, y, r, g, b, size):
	matrix = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
		[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
		[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
	]

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				set_pixel(y - j, x - i, r, g, b, size) """

def MovePlane(x, y, sx, sy,size):
	clearCanvas()
	vertices = Traslate([[x, y, 1]], sx, sy)
	x = vertices[0][0]
	y = vertices[0][1]
	Plane(y, -x, size)
	pygame.display.flip()
	return x, y

### Draw
def display_openGL(width, height, scale):
	pygame.display.set_mode((width, height), pygame.OPENGL)

	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	# glScalef(scale, scale, 0)

	gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)

"""def Plane(x, y, size):
	matrix = [
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0],
		[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,3,0,0],
		[0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,3,3,1,0],
		[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,3,1,3,1,1],
		[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
		[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
		[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
	]

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):

			if matrix[i][j] == 1:
				r,g,b = 144/255,238/255,144/255
				set_pixel(y - j, x - i, r, g, b, size)
			if matrix[i][j] == 2:
				r, g, b = 0,1,1
				set_pixel(y - j, x - i, r, g, b, size)
			if matrix[i][j] == 3:
				r, g, b = 0,255,255
				set_pixel(y - j, x - i, r, g, b, size)"""



def Plane(x, y, size):
	matrix = [
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,1,5,5,5,5,5,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,1,5,5,5,5,1,1,1,1,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,1,5,5,1,1,9,9,9,1,1,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,1,5,5,1,9,9,9,9,9,9,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,1,5,1,9,9,9,1,3,1,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,1,1,1,0,0,1,1,9,1,1,1,3,3,1,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,2,2,2,2,1,1,1,1,1,3,1,3,3,3,3,3,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,2,2,2,2,2,2,1,4,1,9,3,3,3,3,3,3,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,2,2,2,2,2,1,4,4,4,1,1,3,3,3,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,2,2,1,1,4,4,4,4,4,1,3,3,3,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,2,2,1,4,4,1,1,1,4,1,3,3,3,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,2,2,1,4,4,1,3,3,3,1,4,1,1,3,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,2,2,1,4,1,3,3,3,3,1,4,1,1,3,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,2,2,1,4,4,1,3,3,3,3,1,4,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0],
		[1,2,2,1,4,4,1,3,3,3,3,3,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0],
		[1,2,2,1,4,4,1,3,3,3,3,3,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],
		[1,2,1,4,4,4,1,3,3,3,3,3,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,1,1,0],
		[1,2,1,4,4,4,1,1,3,3,3,3,3,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0],
		[0,1,1,1,1,1,0,1,3,3,3,3,3,3,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0],
		[0,0,1,1,3,3,3,3,1,3,3,3,3,3,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
		[0,1,3,3,3,3,3,3,1,1,3,3,3,1,1,3,3,3,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
		[0,1,3,3,3,3,3,3,1,1,1,3,1,1,3,3,3,1,3,3,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
		[0,0,1,3,3,3,3,1,2,2,2,1,1,1,3,3,3,3,3,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0],
		[0,0,1,1,1,1,1,2,2,2,2,1,2,1,1,3,3,3,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,1,2,2,2,2,2,2,2,1,2,2,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,1,2,2,2,2,2,1,1,1,1,2,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,7,7,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,7,7,7,7,7,1,0,0,0,0,1,7,7,7,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,1,7,7,7,1,0,0,0,0,0,1,1,7,7,7,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,7,7,7,7,7,7,1,0,0,0,1,7,7,7,7,7,7,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,7,7,7,7,7,7,7,1,0,0,1,7,7,7,7,7,7,7,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	]


	for i in range(len(matrix)):
		for j in range(len(matrix[0])):

			if matrix[i][j] == 1:
				r,g,b = 0/255,0/255,0/255
				set_pixel(y - j, x - i, r, g, b, size)
			if matrix[i][j] == 2:
				r, g, b = 0/255,100/255,0/255
				set_pixel(y - j, x - i, r, g, b, size)
			if matrix[i][j] == 3:
				r, g, b = 255/255,160/255,122/255
				set_pixel(y - j, x - i, r, g, b, size)
			if matrix[i][j] == 4:
				r, g, b = 255/255,0/255,0/255
				set_pixel(y - j, x - i, r, g, b, size)
			if matrix[i][j] == 5:
				r, g, b = 255/255,255/255,0/255
				set_pixel(y - j, x - i, r, g, b, size)
			if matrix[i][j] == 7:
				r, g, b = 139/255,69/255,19/255
				set_pixel(y - j, x - i, r, g, b, size)
			if matrix[i][j] == 9:
				r, g, b = 255/255,255/255,255/255
				set_pixel(y - j, x - i, r, g, b, size)


def DDA(x0, y0, x1, y1, r, g, b, size):
	points = []
	dx = x1 - x0
	dy = y1 - y0

	x = x0
	y = y0

	if abs(dx) > abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)

	xi = dx / steps
	yi = dy / steps

	set_pixel(round(x), round(y), r, g, b, size)
	points.append((round(x), round(y)))
	for k in range(int(steps)):
		x += xi
		y += yi
		set_pixel(round(x), round(y), r, g, b, size)
		points.append((round(x), round(y)))
	return points

def DrawPolygon(vertices, r, g, b, size):
	# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
	vertices.append(vertices[0])
	for k in range(len(vertices) - 1):
		x0, y0 = vertices[k]
		x1, y1 = vertices[k + 1]
		DDA(x0, y0, x1, y1, r, g, b, size)


def SimpleSeedFill(width, height, size, vertices, xi, yi, r, g, b):
        r, g, b = 255 * r, 255 * g, 255 * b
        stack = []
        stack.append((xi, yi))
        while len(stack) > 0:
                x, y = stack.pop()

                if color_pixel(width, height, x, y, size) != [r, g, b]:
                        set_pixel(x, y, r, g, b, size)
                        #print(x, y)
                # examine surrounding pixels to see if they should be placed onto stack
                if color_pixel(width, height, x + 1, y, size) != [r, g, b] and Validar(width, height, x + 1, y, size,r, g, b):
                        stack.append((x + 1, y))

                if color_pixel(width, height, x + 1, y + 1, size) != [r, g, b] and Validar(width, height, x + 1, y+1, size,r, g, b):
                        stack.append((x + 1, y + 1))
                       

                if color_pixel(width, height, x, y + 1, size) != [r, g, b] and Validar(width, height, x , y+1, size,r, g, b):
                        stack.append((x, y + 1))

                if color_pixel(width, height, x - 1, y + 1, size) != [r, g, b] and Validar(width, height, x - 1, y+1, size,r, g, b):
                        stack.append((x - 1, y + 1))

                if color_pixel(width, height, x - 1, y, size) != [r, g, b] and Validar(width, height, x - 1, y, size,r, g, b):
                        stack.append((x - 1, y))

                if color_pixel(width, height, x - 1, y - 1, size) != [r, g, b] and Validar(width, height, x -1, y-1, size,r, g, b):
                        stack.append((x - 1, y - 1))

                if color_pixel(width, height, x, y - 1, size) != [r, g, b] and Validar(width, height, x + 1, y-1, size,r, g, b):
                        stack.append((x, y - 1))

                if color_pixel(width, height, x + 1, y - 1, size) != [r, g, b] and Validar(width, height, x + 1, y-1, size,r, g, b):
                        stack.append((x + 1, y - 1))


#VALIDACION SI ESTA FUERA O DENTRO DEL CONTORNO 
def Validar(width, height, xi, yi, size,r,g,b):
        inputA=int('0000',2)
        #comparamos si tiene un pixel arriba,abajo,a la izquierda y a la derecha si tiene todos estos requisitos el punto esta en la figura
        for i in range(0,150):
                if color_pixel(width, height, xi+i, yi, size) == [r, g, b]:
                        inputA=inputA | int('0001',2) 
                        break
        for i in range(0,150):
                if color_pixel(width, height, xi, yi+i, size) == [r, g, b]:
                        inputA=inputA | int('0010',2) 
                        break
        for i in range(0,150):
                if color_pixel(width, height, xi-i, yi, size) == [r, g, b]:
                        inputA=inputA | int('0100',2) 
                        break
        for i in range(0,150):
                if color_pixel(width, height, xi, yi-i, size) == [r, g, b]:
                        inputA=inputA | int('1000',2) 
                        break
        return inputA==int('1111',2)