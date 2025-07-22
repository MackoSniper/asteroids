from circleshape import CircleShape
from constants import *
from bullet import Bullet
import pygame

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, shot_cooldown=PLAYER_SHOT_COOLDOWN, remaining_time=0.0):
        super().__init__(x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.rotation = 0.0
        self.shot_cooldown = shot_cooldown
        self.remaining_time = remaining_time

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.remaining_time > 0:
            self.remaining_time -= dt
        else:
            self.remaining_time = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.remaining_time <= 0:
                self.shoot()
                
            
                

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet_position = self.position + forward * (self.radius + SHOT_RADIUS)
        bullet_velocity = forward * PLAYER_SHOT_SPEED
        self.remaining_time = self.shot_cooldown
        Bullet(bullet_position.x, bullet_position.y, SHOT_RADIUS, bullet_velocity)