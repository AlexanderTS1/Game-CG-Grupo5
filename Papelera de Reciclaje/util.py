# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# Python 3.8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import math
import random as rdn
### Algorithm ###
def set_pixel(x, y, r, g, b, size):
    glColor3f(r, g, b)
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    pygame.display.flip()
    # print("{}\t{}".format(x, y))
    pygame.time.wait(10)
def color_pixel(width, height, x, y, size):
    rgb = glReadPixels(width / 2 + x , height / 2 + y, size ,size
    ,
    GL_RGB,
    GL_UNSIGNED_BYTE, None)
return list(rgb)
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
for k in range(steps):
x += xi
y += yi
set_pixel(round(x), round(y), r, g, b, size)
points.append((round(x), round(y)))
return points
def Bressennham(x0, y0, x1, y1, r, g, b, size):
# |m| < 1
dx = abs(x1 - x0)
dy = abs(y1 - y0)
""" if x1 - x0 == 0:
m = 0
else:
m = (y1 - y0) / (x1 - x0) """
r = 2 * dy
s = 2 * dy - 2 * dx
p = 2 * dy - dx
if x0 > x1:
x = x1
y = y1
x1 = x0
else:
x = x0
y = y0
set_pixel(x, y, 1, 0, 0, size)
k = 0
# print(m, dx, dy)
while k < dx:
x += 1
if p < 0:
p = p + r
else:
y += 1
p = p + s
""" if m < 1:#dx == 0:
set_pixel(x, y, r, g, b, size)
else:
set_pixel(x, y, r, g, b, size) """
set_pixel(x, y, r, g, b, size)
k += 1
def Bressennham_(x0, y0, x1, y1, r, g, b, size):
# |m| < 1
dx = abs(x1 - x0)
dy = abs(y1 - y0)
""" if x1 - x0 == 0:
m = 0
else:
m = (y1 - y0) / (x1 - x0) """
r = 2 * dy
s = 2 * dy - 2 * dx
p = 2 * dy - dx
if x0 > x1:
x = x1
y = y1
x1 = x0
else:
x = x0
y = y0
set_pixel(x, y, 1, 0, 0, size)
k = 0
# print(m, dx, dy)
while k < dx:
x += 1
if p < 0:
p = p + r
else:
y += 1
p = p + s
""" if m < 1:#dx == 0:
set_pixel(x, y, r, g, b, size)
else:
set_pixel(x, y, r, g, b, size) """
set_pixel(x, y, r, g, b, size)
k += 1
def Circle2v(xc, yc, radio, r, g, b, size):
# set_pixel(xc + radio, yc, 0, 0, 1, size)
# set_pixel(xc - radio, yc, 0, 1, 0, size)
for x in range(-radio, radio + 1):
y = math.ceil(math.sqrt(radio * radio - x * x))
set_pixel(xc + x, yc + y, r, g, b, size)
set_pixel(xc - x, yc - y, r, g, b, size)
def Circle2vQ(xc, yc, radio, r, g, b, size):
for x in range(-radio, 0):
y = math.ceil(math.sqrt(radio * radio - x * x))
set_pixel(xc + x, yc + y, r, g, b, size)
set_pixel(xc - y, yc - x, r, g, b, size)
def Circle2vQuarter(xc, yc, radio, r, g, b, size):
for x in range(-radio, 0):
y = math.ceil(math.sqrt(radio * radio - x * x))
set_pixel(xc + x, yc + y, r, g, b, size)
for y in range(0, -radio, -1):
x = math.ceil(math.sqrt(radio * radio - y * y))
set_pixel(xc - x, yc - y, r, g, b, size)
def Circle4v(xc, yc, radio, r, g, b, size):
# set_pixel(xc, yc + radio, 0, 1, 0, size)
# set_pixel(xc, yc - radio, 0, 0, 1, size)
for x in range(radio + 1):
root = math.sqrt(radio * radio - x * x)
y = math.ceil(root)
print("{}\t{}\t{}".format(x, y, root))
set_pixel(xc + x, yc + y, r, g, b, size)
""" set_pixel(xc - x, yc + y, r, g, b, size)
set_pixel(xc - x, yc - y, r, g, b, size)
set_pixel(xc + x, yc - y, r, g, b, size) """
def Circulo4(xc, yc, radio, r, g, b, size):
 raiz = math.sqrt(2)
 inicio = math.ceil(radio / raiz)

 for x in range(-inicio, inicio): #-71,70
 y=math.ceil(math.sqrt(radio*radio-x*x))
 print(x, y)
 set_pixel(xc + x, yc + y, r, g, b, size)
 """ set_pixel(xc - x, yc - y, r, g, b, size)
 set_pixel(xc - y, yc + x, r, g, b, size)
 set_pixel(xc + y, yc - x, r, g, b, size) """
def Circle8v(xc, yc, radio, r, g, b, size):
# set_pixel(xc, yc + radio, 0, 1, 0, size)
# set_pixel(xc, yc - radio, 0, 0, 1, size)
# set_pixel(xc + radio, yc, 0, 1, 0, size)
# set_pixel(xc - radio, yc, 0, 0, 1, size)
for x in range(math.ceil(radio / math.sqrt(2)) + 1):
y = math.ceil(math.sqrt(radio * radio - x * x))
set_pixel(xc + x, yc + y, r, g, b, size)
set_pixel(xc - x, yc + y, r, g, b, size)
set_pixel(xc - x, yc - y, r, g, b, size)
set_pixel(xc + x, yc - y, r, g, b, size)
set_pixel(xc + y, yc + x, r, g, b, size)
set_pixel(xc - y, yc + x, r, g, b, size)
set_pixel(xc - y, yc - x, r, g, b, size)
set_pixel(xc + y, yc - x, r, g, b, size)
def CirclePM(xc, yc, radio, r, g, b, size):
# k starting in 0
x = 0
y = radio
p = 1 - radio # (5 / 4) - radio
""" set_pixel(xc + x, yc + y, r, g, b, size)
set_pixel(xc - x, yc + y, r, g, b, size)
set_pixel(xc - x, yc - y, r, g, b, size)
set_pixel(xc + x, yc - y, r, g, b, size)
set_pixel(xc + y, yc + x, r, g, b, size)
set_pixel(xc - y, yc + x, r, g, b, size)
set_pixel(xc - y, yc - x, r, g, b, size)
set_pixel(xc + y, yc - x, r, g, b, size) """
while x < y:
# x += 1
if p < 0:
p += 2 * x + 1
else:
y -= 1
p += 2 * (x - y) + 1
set_pixel(xc + x, yc + y, r, g, b, size)
set_pixel(xc - x, yc + y, r, g, b, size)
set_pixel(xc - x, yc - y, r, g, b, size)
set_pixel(xc + x, yc - y, r, g, b, size)
set_pixel(xc + y, yc + x, r, g, b, size)
set_pixel(xc - y, yc + x, r, g, b, size)
set_pixel(xc - y, yc - x, r, g, b, size)
set_pixel(xc + y, yc - x, r, g, b, size)
x += 1
def Circle(xc, yc, radio, r, g, b, size):
angle = 0
while angle < 45:
x = radio * math.cos(math.radians(angle))
y = radio * math.sin(math.radians(angle))
set_pixel(xc + x, yc + y, r, g, b, size)
set_pixel(xc - x, yc + y, r, g, b, size)
set_pixel(xc - x, yc - y, r, g, b, size)
set_pixel(xc + x, yc - y, r, g, b, size)
set_pixel(xc + y, yc + x, r, g, b, size)
set_pixel(xc - y, yc + x, r, g, b, size)
set_pixel(xc - y, yc - x, r, g, b, size)
set_pixel(xc + y, yc - x, r, g, b, size)
angle += 1 / radio
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
if color_pixel(width, height, x, y, size) != [r, g,
b]:
set_pixel(x, y, r, g, b, size)
print(x, y)
# examine surrounding pixels to see if they should be
placed onto stack
if color_pixel(width, height, x + 1, y, size) != [r,
g, b]:
stack.append((x + 1, y))
if color_pixel(width, height, x + 1, y + 1, size) !=
[r, g, b]:
stack.append((x + 1, y + 1))
if color_pixel(width, height, x, y + 1, size) != [r,
g, b]:
stack.append((x, y + 1))
if color_pixel(width, height, x - 1, y + 1, size) !=
[r, g, b]:
stack.append((x - 1, y + 1))
if color_pixel(width, height, x - 1, y, size) != [r,
g, b]:
stack.append((x - 1, y))
if color_pixel(width, height, x - 1, y - 1, size) !=
[r, g, b]:
stack.append((x - 1, y - 1))
if color_pixel(width, height, x, y - 1, size) != [r,
g, b]:
stack.append((x, y - 1))
if color_pixel(width, height, x + 1, y - 1, size) !=
[r, g, b]:
stack.append((x + 1, y - 1))
def FillTriangle(vertices, r, g, b, size):
# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
x0, y0 = vertices[1]
x1, y1 = vertices[2]
points = DDA(x0, y0, x1, y1, r, g, b, size)
# print(points)
x0, y0 = vertices[0]
print(x0, y0)
for item in points:
x1, y1 = item
print(x1, y1)
DDA(x0, y0, x1, y1, r, g, b, size)
# break
def FillTriangle_(vertices, r, g, b, size):
# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
points = []
vertices.append(vertices[0])
for k in range(len(vertices) - 1):
x0, y0 = vertices[k]
x1, y1 = vertices[k + 1]
point = DDA(x0, y0, x1, y1, r, g, b, size)
points.append(point)
xg = 0
yg = 0
for k in range(len(vertices)):
xg += vertices[k][0]
yg += vertices[k][1]
xg = round(xg / 3)
yg = round(yg / 3)
for item_ in points:
for item in item_:
x1, y1 = item
print(x1, y1)
DDA(xg, yg, x1, y1, r, g, b, size)
# break
### Draw
def display_openGL(width, height, scale):
pygame.display.set_mode((width, height), pygame.OPENGL)
glClearColor(0.0, 0.0, 0.0, 1.0)
glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
# glScalef(scale, scale, 0)
gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height/ 2)








def main():
	scale = 1
	width, height = scale * 200, scale * 200

	pygame.init()
	pygame.display.set_caption('C.G. I')
	
	display_openGL(width, height, scale)
	# glColor3f(1.0, 0, 0)
	x = 0
	y = 0
	set_pixel(x, y, 1, 1, 1, scale)
	# set_pixel(1, 0, 1, 0, 0, scale)
	# set_pixel(1, 1, 0, 1, 0, scale)
	# set_pixel(0, 1, 0, 0, 1, scale)

	# DDA(0, 0, 10, 0, 0/255, 255/255, 0/255, scale)
	# DDA(0, 0, 0, 10, 0/255, 255/255, 0/255, scale)
	# Bressennham(0, 0, 6, 7, 0, 1, 0, scale)
	# Circle2v(0, 0, 50, 255/255, 0/255, 0/255, scale)
	# Circle4v(0, 0, 50, 255/255, 0/255, 0/255, scale)
	# Circulo4(0, 0, 100, 255/255, 0/255, 0/255, scale)
	# Circle8v(0, 0, 100, 255/255, 0/255, 0/255, scale)
	# Circle(0, 0, 50, 255/255, 0/255, 0/255, scale)
	# CirclePM(0, 0, 60, 255/255, 0/255, 0/255, scale)

	# vertices = [(0, 0), (0, 6), (5, 6), (5, 0)]
	# vertices = [(1, 1), (1, 5), (4, 5), (4, 1)]
	# vertices = [(1, 1), (1, 50), (40, 50), (40, 1)]
	# vertices = [(1, 1), (1, 50), (40, 50), (40, 1)]
	# vertices = [(1, 1), (25, 50), (50, 50)]
	# vertices = [(1, 1), (1, 50), (30, 50), (30, 30), (50, 30), (50, 1)]
	vertices = [
		(40, 20), (30, 20), (30, 30), (20, 30), (20, 40), 
		(-20, 40), (-20, 30), (-30, 30), (-30, 20), (-40, 20),
		(-40, -20), (-30, -20), (-30, -30), (-20, -30), (-20, -40),
		(20, -40), (20, -30), (30, -30), (30, -20), (40, -20)
	]

	xi = 20
	yi = 25

	DrawPolygon(vertices, 255/255, 0/255, 0/255, scale)

	SimpleSeedFill(width, height, scale, vertices, xi, yi, 255/255, 0/255, 0/255)

	# rgb = glReadPixels(width/2 +x-1, height/2+y-1, scale, scale, GL_RGB, GL_UNSIGNED_BYTE, None)
	# print(list(rgb))

	# Fill Triangle
	# vertices = [(1, 1), (40, 40), (80, 1)]
	# FillTriangle(vertices, 255/255, 0/255, 0/255, scale)
	# DrawPolygon(vertices, 255/255, 0/255, 0/255, scale)
	print("Finish...")
	glFlush()
	pygame.display.flip()
	 
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

if __name__ == '__main__':
	main()



