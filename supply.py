import pygame
import random


class Supply:  # 补给物品类

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self._bullet_supply_image = pygame.image.load('images/bullet_supply.png')
        self._bullet_supply_rect = self._bullet_supply_image.get_rect()

        self._bullet_supply_rect.x = random.randint(50, 750)
        self._bullet_supply_rect.y = 50

        self.x = float(self._bullet_supply_rect.x)
        self.y = float(self._bullet_supply_rect.y)

    def update(self):   # 位置更新
        self.y += self.settings.supply_speed
        self._bullet_supply_rect.y = self.y

    def draw_supply(self):  # 屏幕上画出
        self.screen.blit(self._bullet_supply_image, self._bullet_supply_rect)

    @property
    def bullet_supply_rect(self):
        return self._bullet_supply_rect
