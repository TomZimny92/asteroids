import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, width=2)

    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self):
        print(f"self.radius: {self.radius}")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print(f"self.radius <= asteroidminradius")
            return
        else:
            print(f"split the asteroid")
            random_angle = random.uniform(20, 50)

            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            split_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_ast2 = Asteroid(self.position.x, self.position.y, new_radius)

            split_ast1.velocity = vector1 * 1.2
            split_ast2.velocity = vector2 * 1.2
