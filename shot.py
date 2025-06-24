import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, position, radius):
        super().__init__(position[0], position[1], SHOT_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, SHOT_RADIUS, width=1)

    def update(self, dt):
        self.position = self.position + self.velocity * dt
