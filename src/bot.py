import math
import pygame
from interfaces import InitObject

class Bot(InitObject):
    def __init__(self, cue_ball, balls, bot_active):
        self.cue_ball = cue_ball
        self.balls = balls
        self.power = 13
        self.bot_active = bot_active
        self.target_ball = 0

    def find_ball(self):
        if self.cue_ball.vx == 0 and self.cue_ball.vy == 0:
            self.target_ball = self.balls[1]
            min_dist = math.sqrt((self.target_ball.x - self.cue_ball.x)**2 + (self.target_ball.y - self.cue_ball.y)**2)
            for ball in self.balls[2:]:
                dist = math.sqrt((ball.x - self.cue_ball.x)**2 + (ball.y - self.cue_ball.y)**2)
                if dist < min_dist:
                    min_dist = dist
                    self.target_ball = ball
    def hit(self):
        if self.cue_ball.vx == 0 and self.cue_ball.vy == 0:
            clock = pygame.time.Clock()
            if self.target_ball:
                dist = math.sqrt((self.target_ball.x - self.cue_ball.x)**2 + (self.target_ball.y - self.cue_ball.y)**2)
                if dist > 0:
                    dir_x = (self.target_ball.x - self.cue_ball.x) / dist
                    dir_y = (self.target_ball.y - self.cue_ball.y) / dist
                    self.cue_ball.vx += self.power * dir_x
                    self.cue_ball.vy += self.power * dir_y
            self.bot_active = False
            clock.tick(3)