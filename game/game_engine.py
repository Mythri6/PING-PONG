import time
import pygame
from .paddle import Paddle
from .ball import Ball

# Game Engine

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100

        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height)

        self.ball.game_engine = self  # so ball can play sounds


        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.max_score = 5  # default, can be changed by replay option

        self.sound_paddle = pygame.mixer.Sound("sounds/paddle_hit.wav")
        self.sound_wall = pygame.mixer.Sound("sounds/wall_bounce.wav")
        self.sound_score = pygame.mixer.Sound("sounds/score.wav")



    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-10, self.height)
        if keys[pygame.K_s]:
            self.player.move(10, self.height)

    def update(self):
        self.ball.move_and_collide(self.player, self.ai)

        if self.ball.x <= 0:
            self.ai_score += 1
            self.sound_score.play()
            self.ball.reset()
        elif self.ball.x >= self.width:
            self.player_score += 1
            self.sound_score.play()
            self.ball.reset()

        self.ai.auto_track(self.ball, self.height)

    def render(self, screen):
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width//2, 0), (self.width//2, self.height))

        # Draw score
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width//4, 20))
        screen.blit(ai_text, (self.width * 3//4, 20))

    def check_game_over(self, screen):
        winner_text = ""
        if self.player_score >= self.max_score:
            winner_text = "Player Wins!"
        elif self.ai_score >= self.max_score:
            winner_text = "AI Wins!"
        else:
            return False  # Game continues

        # Display game over
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 50)
        text_surface = font.render(winner_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2 - 50))
        screen.blit(text_surface, text_rect)

        # Show replay options
        option_font = pygame.font.SysFont("Arial", 30)
        options = [
            "Press 3 for Best of 3",
            "Press 5 for Best of 5",
            "Press 7 for Best of 7",
            "Press ESC to Exit"
        ]
        for i, option in enumerate(options):
            opt_surface = option_font.render(option, True, (255, 255, 255))
            opt_rect = opt_surface.get_rect(center=(self.width // 2, self.height // 2 + 30 + i * 40))
            screen.blit(opt_surface, opt_rect)

        pygame.display.flip()

        # Wait for user input
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        self.max_score = 3
                        waiting = False
                    elif event.key == pygame.K_5:
                        self.max_score = 5
                        waiting = False
                    elif event.key == pygame.K_7:
                        self.max_score = 7
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
            pygame.time.Clock().tick(60)

        # Reset scores and ball for replay
        self.player_score = 0
        self.ai_score = 0
        self.ball.reset()
        return False  # Game continues after replay selection

    

