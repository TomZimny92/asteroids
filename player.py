import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, shots):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        print(f"dt {dt}")
        self.rotation = self.rotation + PLAYER_TURN_SPEED * dt
        print(f"self.rotation {self.rotation}")

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        shot = Shot(self.position, SHOT_RADIUS)
        #print(self.rotation)
        shot_velocity = pygame.Vector2(0,1)
        #print(f"shot_velocity {shot_velocity}")
        shot_velocity.rotate(self.rotation)
        #print(f"shot_velocity {shot_velocity}")
        shot_velocity = shot_velocity * PLAYER_SHOOT_SPEED
        #print(f"shot_velocity {shot_velocity}")
        
        shot.velocity = shot_velocity
        #print(f"shot_velocity {shot_velocity}")
        self.shots.add(shot)
        
