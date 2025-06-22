import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Automatically add to groups if containers are defined
        if hasattr(self.__class__, "containers"):
            super().__init__(*self.__class__.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Subclasses must override
        pass

    def update(self, dt):
        # Subclasses must override
        pass
    
    def collides_with(self, other):
      return self.position.distance_to(other.position) <= self.radius + other.radius

