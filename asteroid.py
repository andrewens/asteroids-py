import pygame
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS
        velocity1 = self.velocity.rotate(-random_angle) * ASTEROID_SPEED_SPLIT_MULTIPLIER
        velocity2 = self.velocity.rotate(random_angle) * ASTEROID_SPEED_SPLIT_MULTIPLIER

        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)

        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2


