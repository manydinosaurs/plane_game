class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False  # 启动时游戏处于非活跃状态

    def reset_stats(self):  # 游戏重开
        self.ships_left = self.settings.ship_limit
        self.score = self.settings.zero_score
        self.bullet_now = self.settings.bullet_allowed
        self.bomb_left = self.settings.bomb_have
