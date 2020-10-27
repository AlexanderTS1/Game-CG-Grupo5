# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

# Reference: https://www.pygame.org/docs/ref/event.html

from utils_ import *

def main():
    scale = 1
    width, height = 400, 400

    pygame.init()
    pygame.display.set_caption('C.G. I')
    
    display_openGL(width, height, scale)
    # glColor3f(1.0, 0, 0)

    # -------
    # Point (pixel)
    # -------
    x = 0
    y = 0
    set_pixel(x, y, 255/255, 255/255, 255/255, scale)

    x, y = 0, 0
    x, y = MoveDefender(x, y, 0, 0, 255/255, 0/255, 0/255, scale)

    print("Finish...")
    glFlush()
    pygame.display.flip()
     
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("K_a")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    print("K_LEFT")
                    sx = 2
                    sy = 0
                    x, y = MoveDefender(x, y, sx, sy, 255/255, 0/255, 0/255, scale)
                elif event.key == pygame.K_RIGHT:
                    print("K_RIGHT")
                    sx = -2
                    sy = 0
                    x, y = MoveDefender(x, y, sx, sy, 255/255, 0/255, 0/255, scale)
                elif event.key == pygame.K_UP :
                    print("K_UP")
                    sx = 0
                    sy = 2
                    x, y = MoveDefender(x, y, sx, sy, 255/255, 0/255, 0/255, scale)
                    set_pixel(50, 50, 255/255, 255/255, 255/255, 3)
                elif event.key == pygame.K_DOWN :
                    print("K_DOWN")
                    sx = 0
                    sy = -2
                    x, y = MoveDefender(x, y, sx, sy, 255/255, 0/255, 0/255, scale)
                                        
if __name__ == '__main__':
    main()
