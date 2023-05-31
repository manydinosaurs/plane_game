import pygame


class Icon:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.game_over_image = pygame.image.load('images/Game_Over.png')  # 游戏结束字体图标
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = (610, 120)

        self.ship_icon_image = pygame.image.load('images/ship_icon.png')  # 飞船图标
        self.ship_icon_rects = []  # 存储飞船图标的矩形对象

        self.bomb_icon_image = pygame.image.load('images/bomb.png')
        self.bomb_icon_rects = []

        for i in range(3):
            ship_icon_rect = self.ship_icon_image.get_rect()
            ship_icon_rect.x = i * 40  # 每个飞船图标之间的水平间距为50
            ship_icon_rect.y = 0
            self.ship_icon_rects.append(ship_icon_rect)

        for j in range(2):
            bomb_icon_rect = self.bomb_icon_image.get_rect()
            bomb_icon_rect.x = j * 40
            bomb_icon_rect.y = 560
            self.bomb_icon_rects.append(bomb_icon_rect)

    def blitme_game_over(self):
        self.screen.blit(self.game_over_image, self.game_over_rect)

    def blitme_ship_icon_at_position(self, index):
        ship_icon_rect = self.ship_icon_rects[index]
        self.screen.blit(self.ship_icon_image, ship_icon_rect)

    def remove_ship_icon(self, index):
        ship_icon_rect = self.ship_icon_rects[index]
        self.screen.fill(self.settings.bg_color, ship_icon_rect)

    def blitme_bomb_icon_at_position(self, index):
        bomb_icon_rect = self.bomb_icon_rects[index]
        self.screen.blit(self.bomb_icon_image, bomb_icon_rect)

