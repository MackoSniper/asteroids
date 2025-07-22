from circleshape import CircleShape
from constants import SHOT_RADIUS
from constants import PLAYER_SHOT_SPEED
import pygame

class Bullet(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt