import pygame
import random
from constants import *
from player import Player
from circleshape import *
from asteroids import *
from asteroidfield import *
from shots import *

clock=pygame.time.Clock()
dt=0
updatable=pygame.sprite.Group()
drawable=pygame.sprite.Group()
asteroids=pygame.sprite.Group()
shots=pygame.sprite.Group()
updatable.add(asteroids)
Player.containers=(updatable, drawable)
Asteroid.containers=(updatable, drawable, asteroids)
AsteroidField.containers=(updatable)
Shot.containers=(shots, updatable, drawable)




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                raise SystemExit
        for shot in shots:
            for asteroid in asteroids:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
                    break

    
            
        

if __name__ == "__main__":
    main()