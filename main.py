import pygame   # this allows us to use code from the open-source pygame library throughout this file
from constants import *

def main():
    pygame.init()  # Initialize pygame

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Event handling - quit if window closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.display.flip()   # Update the display

if __name__ == "__main__":
    main()
