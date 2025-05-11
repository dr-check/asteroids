import pygame
from constants import *
from player import Player
from circleshape import *

clock=pygame.time.Clock()
dt=0
updatable=pygame.sprite.Group()
drawable=pygame.sprite.Group()
Player.containers=updatable, drawable



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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

    
            
        

if __name__ == "__main__":
    main()