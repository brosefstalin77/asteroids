#this allows us to use code from 
#the open-source pygame library
#throughout this file
import pygame
from constants import*
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def  main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Shot.containers = (shots, updatable, drawable)

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroidfield = AsteroidField()


	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	dt = 0
	print("Starting asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)




	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0, 0, 0))

		for update_object in updatable:
			update_object.update(dt)

		for draw_object in drawable:
			draw_object.draw(screen)

		for asteroid_obj in asteroids:
			if asteroid_obj.collision(player):
				print("Game Over!")
				return

			for missile in shots:
				if asteroid_obj.collision(missile):
					missile.kill()
					asteroid_obj.split()


		#player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000
		#player.update(dt)
	

if __name__ == "__main__":
	main()
