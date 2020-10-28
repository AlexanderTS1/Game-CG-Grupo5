from utils3 import *
import pygame

def main():
        print("1.-Dificultad basica")
        print("2.-Dificultad intermedia")
        print("3.-Dificultad avanzada")
        dificultad=int(input("Escoja una dificultad: "))

        if (dificultad==1):
                VidaMaximaMonster=8
        if (dificultad==2):
                VidaMaximaMonster=15
        if (dificultad==3):
                VidaMaximaMonster=30
        scale = 1
        width, height = 800, 800

        pygame.init()
        pygame.display.set_caption('DiMiTri Boss')
        
        pantalla=display_openGL(width, height, scale)
        # glColor3f(1.0, 0, 0)

        # -------
        # Point (pixel)
        # -------


        
        print("Finish...")
        pygame.display.flip()
        clock=pygame.time.Clock()


        xjugador, yjugador = 160,460
        origenbalay=yjugador
        posicion="D"
        contador=4000
        xmovjugador=0
        salto=15
        isJump=False
        isShot=False
        gameOver=False
        posxmonster=500
        posymonster=250
        VidaMaximaHumano=15
        VidaMonster=VidaMaximaMonster
        VidaHumano=15
        #posicion criatura
        posxcriatura=500
        posycriatura=250
        nivel=1


        while not gameOver:
                for event in pygame.event.get():
                        if event.type == QUIT:
                                gameOver=True
                        
                
                if event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_LEFT:
                                xmovjugador=-10
                                posicion="I"
                        if event.key==pygame.K_RIGHT:
                                xmovjugador=10
                                posicion="D"
                        if event.key==pygame.K_SPACE:
                                isJump=True
                        if event.key==pygame.K_f:
                                isShot=True
                if event.type==pygame.KEYUP:
                        if event.key==pygame.K_LEFT:
                                xmovjugador=0
                        if event.key==pygame.K_RIGHT:
                                xmovjugador=0
                        if event.key==pygame.K_f:
                                isShot=isShot

                if isJump:
                        if salto>=-15:
                                yjugador-=(salto*abs(salto))*0.2
                                salto-=1
                        else:
                                salto=15
                                isJump=False
                
                

                if (nivel==1):
                        #NIVEL 1 DEL JUEGO
                        vertices = Traslate([[xjugador, yjugador, 1]], xmovjugador, 0)
                        xjugador = vertices[0][0]
                        yjugador = vertices[0][1]
                        #xjugador+=xmovjugador
                        CampoDeBatalla(20)
                        
                        Soldier(xjugador, yjugador,1,1,1, 2,posicion)
                        #Se necesita canalizar el tiro
                        if isShot:
                                if not abs(origenbalax-xjugador)>500:
                                        
                                        PintaDisparo(origenbalax,origenbalay,2)
                                        origenbalax=origenbalax+20
                                else:
                                        isShot=False
                                        
                        else:
                                origenbalax=xjugador
                                origenbalay=yjugador
                        #Verificar daño hacia el mountruo
                        if abs(origenbalax -posxmonster)<20 and 150<origenbalay<800:
                                VidaMonster=VidaMonster-1
                                print("Vida Monster",VidaMonster)
                                isShot=False
                        #Agonia del mountruo
                        if VidaMonster%2==0:
                                if VidaMonster>15:
                                        PintaMountruoAdolorido(posxmonster-100,posymonster-100,20)
                                else:
                                        PintaMountruoAdolorido(posxmonster,posymonster,15)
                        else:
                                if VidaMonster>15:
                                        PintaMountruo(posxmonster-100,posymonster-100,20)
                                else:
                                        PintaMountruo(posxmonster,posymonster,15)
                        #ataque del monster
                        if (VidaMonster<15):
                                
                                if posxcriatura<0:
                                        posycriatura=rdn.randint(300, 550)
                                        posxcriatura=posxmonster
                                else:
                                        PintaCriatura(posxcriatura,posycriatura,2)
                                        posxcriatura=posxcriatura-20
                        else:
                                if posxcriatura<0:
                                        posycriatura=rdn.randint(300, 550)
                                        posxcriatura=posxmonster
                                else:
                                        PintaCriatura(posxcriatura,posycriatura,2)
                                        posxcriatura=posxcriatura-10
        

                        #verificar daño al soldaditoo :v
                        if abs(xjugador -posxcriatura)<5 and 0<(posycriatura-yjugador)<160:
                                VidaHumano=VidaHumano-1
                                print("Vida humano",VidaHumano)
                        #Mostramos la vida del monster
                        BarraDeVida(400,700,VidaMonster,VidaMaximaMonster,10)
                        
                        #Mostramos la vida del monster
                        #set_pixel( 500, 700, 0/255, 0/255,250/255, 100)
                        BarraDeVida(100,700,VidaHumano,VidaMaximaHumano,10)
                        if (VidaHumano==0):
                                BarraDeVida(400,700,VidaMonster,VidaMaximaMonster,10)
                                BarraDeVida(100,700,VidaHumano,VidaMaximaHumano,10)
                                pygame.display.flip()
                                pygame.time.wait(5000)
                                print("Perdistes")
                                gameOver=True
                        if (VidaMonster==0):
                                BarraDeVida(400,700,VidaMonster,VidaMaximaMonster,10)
                                BarraDeVida(100,700,VidaHumano,VidaMaximaHumano,10)
                                pygame.display.flip()
                                pygame.time.wait(5000)
                                nivel=nivel+1
                                xjugador, yjugador = 160,460
                                posicion="D"
                                contador=4000
                                xmovjugador=0
                                salto=15
                                isJump=False
                                isShot=False
                                gameOver=False
                                posxmonster=500
                                posymonster=350
                                VidaMonster=VidaMaximaMonster
                                VidaHumano=15
                                #posicion criatura
                                posxcriatura=300
                                posycriatura=100
                
                if nivel==2:

                        
                        #NIVEL 1 DEL JUEGO
                        vertices = Traslate([[xjugador, yjugador, 1]], xmovjugador, 0)
                        xjugador = vertices[0][0]
                        yjugador = vertices[0][1]
                        #xjugador+=xmovjugador
                        CampoDeBatalla1(20)
                        
                        Soldier(xjugador, yjugador,1,1,1, 2,posicion)
                        #Se necesita canalizar el tiro
                        if isShot:
                                if not abs(origenbalax-xjugador)>500:
                                        
                                        PintaDisparo(origenbalax,origenbalay,2)
                                        origenbalax=origenbalax+20
                                else:
                                        isShot=False
                                        
                        else:
                                origenbalax=xjugador
                                origenbalay=yjugador
                        #Verificar daño hacia el mountruo
                        if abs(origenbalax -posxmonster)<15 and 350<origenbalay<700:
                                VidaMonster=VidaMonster-1
                                print("Vida Monster",VidaMonster)
                                isShot=False
                        #Agonia del mountruo
                        if VidaMonster%2==0:
                                MountruoPsiquico(posxmonster,posymonster,5)
                        else:
                                MountruoPsiquico(posxmonster,posymonster,5)


                        #ataque del monster
                        if (VidaMonster<15):
                                if posxcriatura<0:
                                        posycriatura=rdn.randint(300, 550)
                                        posxcriatura=posxmonster
                                else:
                                        MountruoPsiquico(posxcriatura,posycriatura,1.5)
                                        posxcriatura=posxcriatura-20
                        else:
                                if posxcriatura<0:
                                        posycriatura=rdn.randint(300, 550)
                                        posxcriatura=posxmonster
                                else:
                                        MountruoPsiquico(posxcriatura,posycriatura,1.5)
                                        posxcriatura=posxcriatura-10
                        #verificar daño al soldaditoo :v
                        if abs(xjugador -posxcriatura)<15 and -80<(posycriatura-yjugador)<80:
                                VidaHumano=VidaHumano-1
                                print("Vida humano",VidaHumano)
                        #Mostramos la vida del monster
                        BarraDeVida(400,700,VidaMonster,VidaMaximaMonster,10)
                        
                        #Mostramos la vida del monster
                        #set_pixel( 500, 700, 0/255, 0/255,250/255, 100)
                        BarraDeVida(100,700,VidaHumano,VidaMaximaHumano,10)
                        if (VidaHumano==0):
                                BarraDeVida(400,700,VidaMonster,VidaMaximaMonster,10)
                                BarraDeVida(100,700,VidaHumano,VidaMaximaHumano,10)
                                pygame.display.flip()
                                pygame.time.wait(5000)
                                print("Perdistes")
                                gameOver=True
                        if (VidaMonster==0):
                                BarraDeVida(400,700,VidaMonster,VidaMaximaMonster,10)
                                BarraDeVida(100,700,VidaHumano,VidaMaximaHumano,10)
                                pygame.display.flip()
                                pygame.time.wait(5000)
                                nivel=nivel+1
                                xjugador, yjugador = 160,460
                                posicion="D"
                                xmovjugador=0
                                salto=15
                                isJump=False
                                isShot=False
                                gameOver=False
                                posxmonster=400
                                posymonster=50
                                VidaMonster=VidaMaximaMonster
                                VidaHumano=15
                                #posicion criatura
                                posxcriatura=500            
                                posycriatura=250
                                
                if nivel==3:
                        #NIVEL 3 DEL JUEGO
                        vertices = Traslate([[xjugador, yjugador, 1]], xmovjugador, 0)
                        xjugador = vertices[0][0]
                        yjugador = vertices[0][1]
                        #xjugador+=xmovjugador
                        CampoDeBatalla2(20)
                        Soldier(xjugador, yjugador,1,1,1, 2,posicion)
                        #Se necesita canalizar el tiro
                        if isShot:
                                if not abs(origenbalax-xjugador)>500:
                                        
                                        PintaDisparo(origenbalax,origenbalay,2)
                                        origenbalax=origenbalax+20
                                else:
                                        isShot=False
                                        
                        else:
                                origenbalax=xjugador
                                origenbalay=yjugador
                        #Verificar daño hacia el mountruo
                        if abs(origenbalax -posxmonster)<10 and 0<origenbalay<400:
                                VidaMonster=VidaMonster-1
                                print("Vida Monster",VidaMonster)
                                isShot=False
                        #Agonia del mountruo
                        if VidaMonster%2==0:
                                Dragon(posxmonster,posymonster,5)
                        else:
                                Dragon(posxmonster,posymonster,5)


                        #ataque del monster
                        if (VidaMonster<15):
                                if posxcriatura<0:
                                        posycriatura=rdn.randint(300, 500)
                                        posxcriatura=posxmonster
                                else:
                                        Dragon(posxcriatura,posycriatura,2)
                                        posxcriatura=posxcriatura-12
                        else:
                                if posxcriatura<0:
                                        posycriatura=rdn.randint(300, 500)
                                        posxcriatura=posxmonster
                                else:
                                        Dragon(posxcriatura,posycriatura,2)
                                        posxcriatura=posxcriatura-10
                        #verificar daño al soldaditoo :v
                        if abs(xjugador -posxcriatura)<15 and -80<(posycriatura-yjugador)<80:
                                VidaHumano=VidaHumano-1
                                print("Vida humano",VidaHumano)
                        #Mostramos la vida del monster
                        BarraDeVida(400,700,VidaMonster,VidaMaximaMonster,10)
                        
                        #Mostramos la vida del humano
                        #set_pixel( 500, 700, 0/255, 0/255,250/255, 100)
                        BarraDeVida(100,700,VidaHumano,VidaMaximaHumano,10)
                        if (VidaHumano==0):
                                BarraDeVida(400,700,VidaMonster,VidaMaximaMonster,10)
                                BarraDeVida(100,700,VidaHumano,VidaMaximaHumano,10)
                                pygame.display.flip()
                                pygame.time.wait(5000)
                                print("Perdistes")
                                gameOver=True
                                
                        if (VidaMonster==0):
                                BarraDeVida(400,700,VidaMonster,VidaMaximaMonster,10)
                                BarraDeVida(100,700,VidaHumano,VidaMaximaHumano,10)
                                pygame.display.flip()
                                pygame.time.wait(5000)
                                
                                nivel=nivel+1
                                xjugador, yjugador = 160,460
                                posicion="D"
                                contador=4000
                                xmovjugador=0
                                salto=15
                                isJump=False
                                isShot=False
                                gameOver=False
                                posxmonster=400
                                posymonster=250
                                VidaMonster=VidaMaximaMonster
                                VidaHumano=15
                                #posicion criatura
                                posxcriatura=500
                                posycriatura=250
                                print("Gano !!!!!!")
                                gameOver=True
                

                
                pygame.display.flip()
                clock.tick(30)

                
        pygame.quit()

if __name__ == '__main__':
        main()


