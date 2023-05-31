import pygame
from pygame.sprite import Sprite


class Bomb(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/bomb.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop  # 炸弹位置位于飞船顶部
        self.y = float(self.rect.y)

    def update(self):   # 管理炸弹位置
        self.y -= self.settings.bomb_speed  # 顶部是0 所以是减
        self.rect.y = self.y    # 更新

    def draw_bomb(self):   # 绘制炸弹
        self.screen.blit(self.image, self.rect)


