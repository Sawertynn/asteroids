import pygame
import random

from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius, velocity)
        self.color = "red"
        self.width = 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        x, y = self.position
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        rotate_angle = random.uniform(30, 60)
        velo_base = self.velocity * 1.3
        velo1 = velo_base.rotate(rotate_angle)
        velo2 = velo_base.rotate(-rotate_angle)
        Asteroid(x, y, new_radius, velo1)
        Asteroid(x, y, new_radius, velo2)
