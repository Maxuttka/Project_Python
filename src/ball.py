import pygame
import math
from interfaces import MoveObject, DrawObject, InitObject
from screen import screen

class Ball(MoveObject, DrawObject, InitObject):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = color
        self.vx = 0
        self.vy = 0
        self.mu = 0.01
        self.g = 9.81
        self.dt = 0.08
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def move(self):
        a = self.mu * self.g
        speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
        if speed > 0:
            delta_v = a * self.dt
            if speed - delta_v > 0:
                koef = (speed - delta_v) / speed
                self.vx *= koef
                self.vy *= koef
            else:
                self.vx = 0
                self.vy = 0
        self.x += self.vx
        self.y += self.vy
    def balls_collision(self, other):
        dist = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        if dist < 2*self.radius:
            normal_x = (other.x - self.x) / dist
            normal_y = (other.y - self.y) / dist
            v1_normal = self.vx * normal_x + self.vy * normal_y
            v2_normal = other.vx * normal_x + other.vy * normal_y
            self.vx += (v2_normal - v1_normal) * normal_x
            self.vy += (v2_normal - v1_normal) * normal_y
            other.vx += (v1_normal - v2_normal) * normal_x
            other.vy += (v1_normal - v2_normal) * normal_y
            overlap = (self.radius + other.radius) - dist
            self.x -= overlap / 2
            self.y -= overlap / 2
            other.x += overlap / 2
            other.y += overlap / 2