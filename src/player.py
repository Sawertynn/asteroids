import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.color = "white"
        self.width = 2
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        x, y = self.position
        _ = Shot(x, y, velocity=shot_velocity)

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), self.width)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # turn left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # turn right
            self.rotate(dt)
        if keys[pygame.K_w]:
            # move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # move backward
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # shoot a shot
            if self.shoot_timer == 0:
                self.shoot()
                self.shoot_timer = PLAYER_SHOOT_COOLDOWN
                
        
        self.shoot_timer = max(0, self.shoot_timer - dt)
