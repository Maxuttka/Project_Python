import pygame
import math
from interfaces import MoveObject, DrawObject, InitObject
from screen import screen

class Cue(MoveObject, DrawObject, InitObject):
    def __init__(self, ball, mouse_pos):
        self.x, self.y = mouse_pos
        self.length = 200
        self.ball = ball
    def draw(self):
        if self.ball.vx == 0 and self.ball.vy == 0:
            alpha = math.atan2(self.y - self.ball.y, self.x - self.ball.x)
            cue_end_x = self.ball.x + (self.ball.radius + 10) * math.cos(alpha)
            cue_end_y = self.ball.y + (self.ball.radius + 10) * math.sin(alpha)
            cue_start_x = self.ball.x + (self.length + self.ball.radius) * math.cos(alpha)
            cue_start_y = self.ball.y + (self.length + self.ball.radius) * math.sin(alpha)
            pygame.draw.line(screen, (100,40,0), (cue_start_x, cue_start_y), (cue_end_x, cue_end_y), 7)
    def move(self, mouse_pos):
        self.x, self.y = mouse_pos
    def hit(self):
        dist = math.sqrt((self.ball.x - self.x)** 2 + (self.ball.y - self.y)** 2)
        if dist > 0:
            direction_x = (self.ball.x - self.x) / dist
            direction_y = (self.ball.y - self.y) / dist
            self.ball.vx += 13 * direction_x
            self.ball.vy += 13 * direction_y