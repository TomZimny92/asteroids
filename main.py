#this allows us to use code form the open-source pygame library throughout this file
import pygame
from player import *
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    try:
        pygame.init()
    except:
        print("Game initialization failed.")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

    clock = pygame.time.Clock()
    dt = 0

    gameLoop = True
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    player.draw(screen)

if __name__ == "__main__":
    main()

