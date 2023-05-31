import pygame


class Settings:
    def __init__(self):
        self.screen_width = 800  # 长
        self.screen_height = 600  # 高
        self.bg_color = (200, 230, 230)  # 背景颜色

        self.bullet_speed = 1.0  # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        self.bomb_width = 100   # 炸弹设置
        self.bomb_height = 100
        self.bomb_speed = 1.0
        self.bomb_have = 2

        self.alien_speed = 0.1  # 外星人设置
        self.alien_points = 1

        self.ship_limit = 2  # 飞船设置：三条命
        self.ship_speed = 0.5  # 初始速度

        self.alien_spawn_timer = 0  # 外星人生成计数器
        self.alien_spawn_delay = 2000  # 外星人生成延迟，控制生成的间隔
        self.spawn_probability = 0.001  # 初始概率值

        self.zero_score = 0  # 初始零分

        self.supply_speed = 0.1   # 补给掉落速度

        self.start_time = 0     # 起始时间

