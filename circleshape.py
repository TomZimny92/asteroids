import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else: 
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def hasColided(self, obj):
        distance = pygame.math.Vector2.distance_to(self.position, obj.position)
        r1 = self.radius
        r2 = obj.radius
        if (distance <= r1 + r1):
            return True
        return False 
