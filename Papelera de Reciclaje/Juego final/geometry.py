import pygame,sys
pygame.init()

ancho=800
alto=700
width=5
height=5
esmeralda=(87,181,190)
red=(255,0,0)
x=50
y=490

vel=0
salto=10
isJump=False


ventana=pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Saltando")
clock=pygame.time.Clock()

gameOver=False
while not gameOver:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameOver=True
    if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                vel=-3
            if event.key==pygame.K_RIGHT:
                vel=3
            if event.key==pygame.K_SPACE:
                isJump=True
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_LEFT:
            vel=0
        if event.key==pygame.K_RIGHT:
            vel=0
    if isJump:
        if salto>=-10:
            y-=(salto*abs(salto))*0.5
            salto-=1
        else:
            salto=10
            isJump=False
    x+=vel
    ventana.fill(esmeralda)

    pygame.draw.rect(ventana,red,(x,y,20,20))

    pygame.display.flip()

    clock.tick(60)

pygame.quit() 
