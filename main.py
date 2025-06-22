import pygame   # this allows us to use code from the open-source pygame library throughout this file
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # Delta time (in seconds)

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Containers
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable

    # Create player in the center of the screen and the Asteroid Field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    running = True
    while running:
        # Event handling - quit if window closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update all updatable sprites
        updatable.update(dt)

        screen.fill((0, 0, 0))  # Fill screen with black

        # Draw all drawable sprites
        for sprite in drawable:
            sprite.draw(screen)
            
        pygame.display.flip()   # Update the display

        # Limit to 60 FPS and get delta time
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
