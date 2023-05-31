import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings

        self.rect.x = self.rect.width  # 外星人飞船出现在左上角
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_speed
        self.rect.y = self.y
