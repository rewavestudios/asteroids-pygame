import pygame   # this allows us to use code from the open-source pygame library throughout this file
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot  # Import Shot class

def main():
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # Delta time (in seconds)

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

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

        # Collision detection: Check if player collides with any asteroid
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                exit()  # Or use sys.exit() if you've imported sys
                
            for shot in shots:  # Collision detection: Bullets vs Asteroids
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                
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
