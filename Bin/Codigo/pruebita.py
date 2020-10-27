from utils import *
import pygame, sys
scale = 3
scale = 3
width, height = scale * 200, scale * 200
pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 700), 0, 32)
pygame.display.set_caption('Mostrito_Moviendose')
Bressennham(0, 0, 6, 7, 0, 1, 0, scale)
