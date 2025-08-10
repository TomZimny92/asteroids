# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    asteroid_field = AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player1.cooldown <= 0:
                player1.shoot()
        for ast in asteroids:            
            if ast.hasColided(player1):
                print("Game over!")
                return
            for shot in shots:
                if shot.hasColided(ast):
                    shot.kill()
                    ast.kill()
        updatable.update(dt)
        for s in shots:
            s.update(dt)
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000
if __name__ == "__main__":
    main()
