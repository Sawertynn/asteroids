import pygame
from typing import Optional

class CircleShape(pygame.sprite.Sprite):
    def __init__(
        self, x: float, y: float, radius: float, velocity: Optional[pygame.Vector2] = None
    ):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = velocity or pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.surface.Surface):
        # sub-classes must override
        pass

    def update(self, dt: float):
        # sub-classes must override
        pass

    def check_collision(self, another: "CircleShape") -> bool:
        distance = self.position.distance_to(another.position)
        return distance <= self.radius + another.radius
