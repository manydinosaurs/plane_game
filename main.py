import pygame
import random
import sys
import time
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import *
from icon import Icon
from scoreboard import Scoreboard
from bomb import Bomb
from supply import Supply


class GameInvasion:  # 管理游戏资源和行为

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # 大小
        pygame.display.set_caption("test game")  # 名称
        self.stats = GameStats(self)  # 存储游戏信息的实例
        self.sb = Scoreboard(self)  # 创建计分板实例
        self.ship = Ship(self)  # 飞船创建
        self.bullets = pygame.sprite.Group()  # 创建子弹编组
        self.bombs = pygame.sprite.Group()  # 创建炸弹编组
        self.aliens = pygame.sprite.Group()  # 创建外星人飞船编组
        self.supply = Supply(self)  # 补给品创建
        self.play_button = PlayButton(self, "Play")  # 创建Play按钮
        self.quit_button = QuitButton(self, "Quit")  # 创建Quit按钮
        self.play_again_button = Play_Again_Button(self, "Play Again")  # Play Again按钮
        self.icon = Icon(self)  # 游戏内各种图标建立
        self.last_update_time = time.time()  # 记录上次更新时间

    def run_game(self):  # 运行游戏主循环
        while True:
            self._check_events()  # 按键
            if self.stats.game_active:
                self._probability_control()  # 概率控制
                self.ship.update()  # 移动
                self._update_bullet()  # 更新子弹位置 + 删除到顶子弹
                self._update_bomb()  # 更新炸弹位置
                self._update_aliens()  # 更新外星人位置
                self._create_random_alien()
                if self._time_control():
                    self._update_supply()

            self._update_screen()  # 屏幕显示

    def _check_events(self):  # 按键事件&点击屏幕事件
        for event in pygame.event.get():  # 关闭
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击屏幕
                mouse_pos = pygame.mouse.get_pos()
                self._check_button(mouse_pos)
            # 运动
            elif event.type == pygame.KEYDOWN:  # 按下方向键
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # 松开方向键
                self._check_keyup_events(event)

    def _check_button(self, mouse_pos):  # 检查按键是Play/Quit/Play Again
        if self.play_button.rect.collidepoint(mouse_pos):  # 若鼠标单击Play
            if self.stats.ships_left == 0:
                self._restart_game()
            else:
                self.stats.game_active = True
        elif self.quit_button.rect.collidepoint(mouse_pos):  # 若鼠标单机Quit
            if self.stats.game_active == False or self.stats.ships_left == 0:
                sys.exit()
        elif self.play_again_button.rect.collidepoint(mouse_pos):  # 若鼠标单机Play Again
            if self.stats.ships_left == 0:
                self._restart_game()

    def _restart_game(self):  # 点击Play Again后游戏重启设置
        self.stats.game_active = True  # 游戏状态设为True
        self.stats.score = self.settings.zero_score  # 重置分数
        self.sb.show_score()  # 绘制计分板
        pygame.display.flip()

        self.bullets.empty()  # 清空子弹
        self.aliens.empty()  # 清空外星人
        self._create_random_alien()  # 设置新外星人舰队
        self.ship.center_ship()  # 居中飞船
        self.stats.ships_left = self.settings.ship_limit  # 重置飞船数量
        self.stats.bullet_now = self.settings.bullet_allowed    # 重置子弹数量
        self.stats.bomb_left = self.settings.bomb_have  # 重置炸弹数量
        self.alien_spawn_timer = 0  # 重置外星人生成计时器

    def _check_keydown_events(self, event):  # 按下方向键的方法
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:  # Esc退出
            sys.exit()
        elif event.key == pygame.K_a:
            self._fire_bullet()  # 按下A发射子弹
        elif event.key == pygame.K_SPACE:
            self._fire_bomb()  # 按下空格发射导弹
        else:
            pass  # 按下其他键无反应

    def _check_keyup_events(self, event):  # 松开方向键的方法
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):  # 创建一颗子弹加入编组bullets中
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _fire_bomb(self):  # 创建一个炸弹加入编组bomb中
        if self.settings.bomb_have >= 1:
            new_bomb = Bomb(self)
            self.bombs.add(new_bomb)
            self.settings.bomb_have = self.settings.bomb_have - 1

    def _update_bullet(self):
        self.bullets.update()  # 更新子弹位置
        for bullet in self.bullets.copy():  # 删除到顶的子弹
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _update_bomb(self):
        self.bombs.update()  # 更新位置
        for bomb in self.bombs.copy():  # 删除到顶的炸弹
            if bomb.rect.bottom <= 0:
                self.bombs.remove(bomb)
        self._check_bomb_alien_collisions()

    def _check_bomb_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bombs, self.aliens, True, True)
        num_aliens_destroyed = 0  # 计分用的变量，初始化为0
        if collisions:
            self.aliens.empty()  # 清空外星人编组
            self.stats.score += 5  # 炸弹清除只加5分
            self.sb.prep_score()  # 更新计分板
        if not self.aliens:  # 创建新外星人
            self._create_random_alien()  # 由于外星人是在该方法末尾被消灭的，所以在这里创建新的

    def _update_aliens(self):  # 更新外星人位置
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):  # 外星人和飞船碰撞检测
            self._ship_hit()
        self._check_aliens_bottom()  # 检查外星人到底端

    def _check_bullet_alien_collisions(self):  # 子弹与外星人碰撞检查
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)  # 子弹和外星人碰撞检测
        if collisions:  # 消灭外星人加分
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
        if not self.aliens:  # 创建新外星人
            self._create_random_alien()  # 由于外星人是在该方法末尾被消灭的，所以在这里创建新的

    def _create_random_alien(self):  # 添加随机出现的外星人
        self.settings.alien_spawn_timer += 1
        if self.settings.alien_spawn_timer >= self.settings.alien_spawn_delay:
            if random.randint(0, 1000) < self.settings.spawn_probability:
                alien = Alien(self)
                alien_width = alien.rect.width
                screen_width = self.settings.screen_width
                alien.x = random.randint(0, screen_width - alien_width)  # 在屏幕最上方随机生成外星人x坐标
                alien.rect.x = alien.x
                alien.rect.y = alien.rect.height  # y设为外星人高度
                self.aliens.add(alien)
                self.alien_spawn_timer = 0

    def _probability_control(self):  # 控制概率的量-即游戏难度逐渐增加
        current_time = time.time()
        time_elapsed = current_time - self.last_update_time
        if time_elapsed >= 10:
            self.settings.spawn_probability *= 2
            self.last_update_time = current_time

    def _time_control(self):    # 控制时间
        current_time = time.time()
        time_elapsed = current_time - self.last_update_time
        if 9.5 <= time_elapsed < 10.5 or 19.5 <= time_elapsed < 20.5:
            return True
        return False

    def _check_aliens_bottom(self):  # 检查外星人到屏幕底端
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):  # 外星人飞船碰撞检测
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1  # 余下飞船数量减1
            self.aliens.empty()  # 清空外星人
            self.bullets.empty()  # 清空子弹
            self._create_random_alien()  # 创建新外星人舰队
            self.ship.center_ship()  # 居中新飞船
            sleep(0.5)  # 暂停0.5秒
        else:
            self.stats.game_active = False

    def _update_supply(self):  # 更新补给品位置
        self.supply.update()
        if self.supply.bullet_supply_rect.colliderect(self.ship.rect):
            self._ship_level_up()

    def _ship_level_up(self):  # 飞船升级
        self.settings.bullet_allowed += 2  # 子弹数量+2

    def _update_screen(self):  # 更新屏幕图像，切换新屏幕
        self.screen.fill(self.settings.bg_color)  # 背景颜色
        self.ship.blitme()  # 绘制飞船
        for i in range(self.stats.ships_left):  # 绘制飞船图标
            self.icon.blitme_ship_icon_at_position(i)
        for j in range(self.settings.bomb_have):  # 绘制飞船图标
            self.icon.blitme_bomb_icon_at_position(j)
        for bullet in self.bullets.sprites():  # 绘制子弹
            bullet.draw_bullet()
        for bomb in self.bombs.sprites():   # 绘制炸弹
            bomb.draw_bomb()
        self.aliens.draw(self.screen)  # 绘制外星人
        if self._time_control():
            self.supply.draw_supply()   # 绘制补给品
        self.sb.show_score()  # 绘制计分板
        if not self.stats.game_active and self.stats.ships_left > 0:  # 绘制Play按钮
            self.play_button.draw_button()
        if not self.stats.game_active:  # 绘制Quit按钮
            self.quit_button.draw_button()
        if not self.stats.game_active and self.stats.ships_left == 0:  # 绘制Play Again按钮 + Game Over!
            self.play_again_button.draw_button()
            self.icon.blitme_game_over()
        pygame.display.flip()


if __name__ == '__main__':
    ai = GameInvasion()
    ai.run_game()
