import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, ASTEROID_MIN_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, ASTEROID_MIN_RADIUS, width=2)

    def update(self, dt):
        self.position = self.position + self.velocity * dt
