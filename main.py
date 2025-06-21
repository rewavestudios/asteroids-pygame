import pygame   # this allows us to use code from the open-source pygame library throughout this file
from constants import *

def main():
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # Delta time (in seconds)

    while True:
        # Event handling - quit if window closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.display.flip()   # Update the display

        # Limit to 60 FPS and get delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
