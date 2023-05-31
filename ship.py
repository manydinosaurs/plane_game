import pygame


class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.png')  # 图标初始化
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)  # 速度初始化

        self.moving_left = False  # 初始化移动False，按键时为True
        self.moving_right = False

    def update(self):  # 移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):  # 在屏幕上绘制初始化的图标
        self.screen.blit(self.image, self.rect)

    def center_ship(self):      # 剧中飞船，用于飞船损毁后重生
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
