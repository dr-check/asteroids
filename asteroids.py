import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x=x
        self.y=y
        self.radius=radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        old_radius=self.radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        vector1=self.velocity.rotate(random_angle)
        vector2=self.velocity.rotate(-random_angle)
        asteroid1=Asteroid(self.position.x, self.position.y, old_radius-ASTEROID_MIN_RADIUS)
        asteroid2=Asteroid(self.position.x, self.position.y, old_radius-ASTEROID_MIN_RADIUS)
        asteroid1.velocity=vector1
        asteroid2.velocity=vector2
        

        

