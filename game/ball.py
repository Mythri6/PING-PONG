import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

    def move_and_collide(self, player, ai):
        # Move first
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce off top and bottom walls
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            if hasattr(self, "game_engine"):  # reference to play sound
                self.game_engine.sound_wall.play()
        ball_rect = self.rect()

        # Check collision with player paddle
        if ball_rect.colliderect(player.rect()):
            self.x = player.x + player.width  # prevent sticking inside
            self.velocity_x *= -1
            if hasattr(self, "game_engine"):
                self.game_engine.sound_paddle.play()

        # Check collision with AI paddle
        elif ball_rect.colliderect(ai.rect()):
            self.x = ai.x - self.width  # prevent sticking inside
            self.velocity_x *= -1
            if hasattr(self, "game_engine"):
                self.game_engine.sound_paddle.play()

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
