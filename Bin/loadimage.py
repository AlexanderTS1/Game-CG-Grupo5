import pygame
from pygame.locals import *
 
pygame.init()
 
pantalla = pygame.display.set_mode((340,280))
 
imagen = pygame.image.load("git1.png")
 
 
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pantalla.blit(imagen,(100,100))
    pygame.display.update()
