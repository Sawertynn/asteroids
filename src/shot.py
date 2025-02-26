import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS, velocity)
        self.color = "white"
        self.width = 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.width)

    def update(self, dt):
        self.position += self.velocity * dt
