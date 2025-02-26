import pygame
# from constants import ASTEROID_KINDS, ASTEROID_SPAWN_RATE
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = "red"
        self.width = 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.width)

    def update(self, dt):
        self.position += self.velocity * dt
