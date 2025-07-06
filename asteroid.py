import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Destroy the current asteroid
        self.kill()

        # If it's already at the minimum size, just disappear
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random angle of the split (between 20 and 50 degrees)
        random_angle = random.uniform(20, 50)

        # Rotate velocity to get two new directions
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(-random_angle)

        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the two new asteroids and assign their velocities (slightly faster)
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vel1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vel2 * 1.2