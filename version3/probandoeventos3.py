from prueba import *


def main():
	scale = 1
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

	x, y = -40,50
	

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
				sx = 20
				sy = 0
				CampoDeBatalla(20)
				x, y = MoveDefender(x, y, sx, sy,59/255, 131/255, 189/255, scale)
			elif event.key == pygame.K_RIGHT:
				print("K_RIGHT")
				sx = -20
				sy = 0
				CampoDeBatalla(20)
				x, y = MoveDefender(x, y, sx, sy, 59/255, 131/255, 189/255, scale)
			elif event.key == pygame.K_UP :
				print("K_UP")
				sx = 0
				sy =20
				CampoDeBatalla(20)
				x, y = MoveDefender(x, y, sx, sy,59/255, 131/255, 189/255, scale)
				set_pixel(50, 50, 255/255, 255/255, 255/255, 3)
			elif event.key == pygame.K_DOWN :
				print("K_DOWN")
				sx = 0
				sy = -20
				CampoDeBatalla(20)
				x, y = MoveDefender(x, y, sx, sy, 59/255, 131/255, 189/255, scale)
				
if __name__ == '__main__':
	main()
