import pygame.font


class PlayButton:
    def __init__(self, ai_game, msg):  # 初始化按钮属性
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 120, 60  # 按钮属性
        self.button_color = (0, 255, 127)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont('Impact', 48)  # None:默认字体，48：字号

        self.rect = pygame.Rect(0, 0, self.width, self.height)  # 按钮位置
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):  # 将msg渲染为图像并在按钮上居中
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):  # 显示按钮到屏幕上
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class QuitButton:  # 开始界面退出按钮
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 120, 60  # 按钮属性
        self.button_color = (0, 255, 127)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont('Impact', 48)  # None:默认字体，48：字号

        self.rect = pygame.Rect(340, 380, self.width, self.height)  # 按钮位置

        self._prep_msg(msg)

    def _prep_msg(self, msg):  # 将msg渲染为图像并在按钮上居中
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):  # 显示按钮到屏幕上
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Play_Again_Button:   # 游戏结束按钮
    def __init__(self, ai_game, msg):  # 初始化按钮属性
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 120, 60  # 按钮属性
        self.button_color = (0, 255, 127)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont('Impact', 26)  # None:默认字体，26：字号

        self.rect = pygame.Rect(0, 0, self.width, self.height)  # 按钮位置
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):  # 将msg渲染为图像并在按钮上居中
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):  # 显示按钮到屏幕上
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
