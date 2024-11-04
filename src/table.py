import pygame
from interfaces import DrawObject, InitObject
import math
from screen import screen


class Table(DrawObject, InitObject):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pockets = [
            (0, 0),
            (self.width // 2, 0),
            (self.width, 0),
            (0, self.height),
            (self.width // 2, self.height),
            (self.width, self.height)
        ]
        self.pocket_radius = 20
    def draw(self):
        pygame.draw.rect(screen, (0, 128, 0), (0, 0, self.width, self.height))
        for pocket in self.pockets:
            pygame.draw.circle(screen, (0, 0, 0), pocket, self.pocket_radius)
    def wall_collision(self, ball):
        if ball.x - ball.radius < 0:
            ball.vx *= -1
        elif ball.x + ball.radius > self.width:
            ball.vx *= -1
        if ball.y - ball.radius < 0:
            ball.vy *= -1
        elif ball.y + ball.radius > self.height:
            ball.vy *= -1
    def pocket_collision(self, ball):
        for pocket_x, pocket_y in self.pockets:
            dist = math.sqrt((ball.x - pocket_x) ** 2 + (ball.y - pocket_y) ** 2)
            if dist < self.pocket_radius:
                return True
        return False