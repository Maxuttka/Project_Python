import pygame
from ball import Ball
from cue import Cue
from table import Table
from bot import Bot
from interfaces import DrawObject, InitObject
from screen import screen

class Game(DrawObject, InitObject):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.table = Table(width, height)
        self.cue_ball = Ball(width / 4,height / 2,(255, 255, 255))
        self.balls = [self.cue_ball] + self.triangle()
        self.cue = Cue(self.cue_ball, (width / 2, height / 2))
        self.run = True
        self.bot = Bot(self.cue_ball, self.balls, False)
        self.player_score = 0
        self.bot_score = 0
        self.player_turn = True

    def triangle(self):
        balls = []
        colors = [
            (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), 
            (255, 165, 0), (128, 0, 128), (0, 255, 255), (255, 192, 203),
            (173, 216, 230), (255, 20, 147), (75, 0, 130), (255, 69, 0),
            (34, 139, 34)
        ]
        for row in range(4):
            for col in range(row + 1):
                x = 560 + col * 2 * 10 - row * 10
                y = 160 + row * 10 * 2
                if colors:
                    color = colors.pop(0)
                else: (200, 200, 200)
                balls.append(Ball(x, y, color))
        balls.append(Ball(560, 160 + 5 * 10, (0, 0, 0)))
        return balls
    
    def reset_cue_ball(self):
        self.cue_ball.x = self.width / 4
        self.cue_ball.y = self.height / 2
        self.cue_ball.vx = 0
        self.cue_ball.vy = 0

    def balls_stop(self):
        for ball in self.balls:
            if not ball.is_stop():
                return False
        return True

    def update(self):
        i = 0
        self.cue.move(pygame.mouse.get_pos())
        for ball in self.balls:
            ball.move()
            if self.table.pocket_collision(ball):
                if ball == self.cue_ball:
                    self.reset_cue_ball()
                elif ball.color == (0, 0, 0):
                    self.game_over()
                    self.__init__(self.width, self.height)
                    return
                elif len(self.balls) == 3:
                    self.__init__(self.width, self.height)
                    return
                else:
                    self.balls.remove(ball)
                    if self.player_turn:
                        self.player_score += 1
                    else:
                        self.bot_score += 1
            self.table.wall_collision(ball)
        for ball1 in self.balls:
            for ball2 in self.balls[i+1:]:
                ball1.balls_collision(ball2)
            i+=1

    def input(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONUP and self.balls_stop():
                    self.cue.hit()
                    self.bot.bot_active = True
                    self.player_turn = True


    def game_loop(self):
        clock = pygame.time.Clock()
        while self.run:
            self.input()
            if self.bot.bot_active and self.balls_stop():
                self.bot.find_ball()
                self.bot.hit()
                self.player_turn = False
            self.update()
            self.draw()
            pygame.display.flip()
            clock.tick(60)

    def draw(self):
        self.table.draw()
        for ball in self.balls:
            ball.draw()
        self.cue.draw()
        font = pygame.font.Font(None, 36)
        player_score_text = font.render(f"Игрок: {self.player_score}", True, (255, 255, 255))
        bot_score_text = font.render(f"Бот: {self.bot_score}", True, (255, 255, 255))
        screen.blit(player_score_text, (15, 15))
        screen.blit(bot_score_text, (15, 50))

    def game_over(self):
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 - text.get_height() / 2))
        pygame.display.flip()
        pygame.time.delay(2000)

pygame.init()
game = Game(850, 450)
game.game_loop()
