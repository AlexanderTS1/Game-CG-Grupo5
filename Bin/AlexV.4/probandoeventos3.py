from utils3 import *


def main():
        scale = 2
        width, height = 800, 800

        pygame.init()
        pygame.display.set_caption('Juego grupo 5')
        
        display_openGL(width, height, scale)
        # glColor3f(1.0, 0, 0)

        # -------
        # Point (pixel)
        # -------
        x = 0
        y = 0
        set_pixel(x, y, 255/255, 255/255, 255/255, scale)

        x, y = 160,500
        

        print("Finish...")
        glFlush()
        pygame.display.flip()
        xm=200
        ym=200
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
                                sx = -10*scale
                                sy = 0*scale
                                CampoDeBatalla(20)
                                x, y = MoveDefenderI(x, y, sx, sy,59/255, 131/255, 189/255, scale)
                                
                                pygame.display.flip()
                        elif event.key == pygame.K_RIGHT:
                                print("K_RIGHT")
                                sx = 10*scale
                                sy = 0**scale
                                CampoDeBatalla(20)
                                x, y = MoveDefenderD(x, y, sx, sy, 59/255, 131/255, 189/255, scale)
                                
                                pygame.display.flip()
                        elif event.key == pygame.K_UP:
                                print("K_UP")
                                if(scale==2):
                                        scale=1
                                else:
                                        scale=2
                                x, y = MoveDefenderD(x, y, 0, 0, 59/255, 131/255, 189/255, scale)
                                pygame.display.flip()

                        """     
                        elif event.key == pygame.K_UP :
                                print("K_UP")
                                sx = 0
                                sy =20
                                CampoDeBatalla(20)
                                x, y = MoveDefenderD(x, y, sx, sy,59/255, 131/255, 189/255, scale)
                                set_pixel(50, 50, 255/255, 255/255, 255/255, 3)
                                pygame.display.flip()
                        
                        elif event.key == pygame.K_DOWN :
                                print("K_DOWN")
                                sx = 0
                                sy = -20
                                CampoDeBatalla(20)
                                x, y = MoveDefenderD(x, y, sx, sy, 59/255, 131/255, 189/255, scale)
                                pygame.display.flip()
                        """
                        
if __name__ == '__main__':
        main()
