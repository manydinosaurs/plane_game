import pygame.font


class Scoreboard:  # 得分类

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (0, 0, 204)  # 文本颜色
        self.font = pygame.font.SysFont('Impact', 40)  # 文本字体及大小

        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)  # 得分转换为图像
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()  # 屏幕右上角显示得分
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 15

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)  # 显示得分
