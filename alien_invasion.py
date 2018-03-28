# import sys

import pygame
from pygame.sprite import Group

import game_functions as gf
# from alien import Alien
from settings import Settings
from ship import Ship


class Game():
    def __init__(self, ai_settings):
        # 初始化游戏
        pygame.init()
        # 导入设置
        self.settings = ai_settings
        # 设置屏幕
        self.screen = pygame.display.set_mode((ai_settings.screen_width,
                                               ai_settings.screen_height))
        pygame.display.set_caption(ai_settings.caption)
        # 创建飞船，外星人， 子弹群组
        self.ship = Ship(self.screen, self.settings)
        self.bullets = Group()
        self.aliens = Group()
        gf.creat_fleet(ai_settings, self.screen, self.aliens)

    def run_game(self):
        # 开始游戏主循环
        while True:
            # 监视键盘和鼠标事件
            gf.check_events(self.settings, self.screen, self.ship,
                            self.bullets)
            # 让最近绘制的屏幕可见
            self.ship.update()
            gf.update_bullets(self.bullets)
            gf.update_screen(self.settings, self.screen, self.ship,
                             self.bullets, self.aliens)


if __name__ == '__main__':
    ai_settings = Settings()
    new_game = Game(ai_settings)
    new_game.run_game()
