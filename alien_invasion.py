# import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


class Game():
    def __init__(self, ai_settings):
        # 初始化游戏
        pygame.init()
        # 导入设置
        self.settings = ai_settings
        self.screen = pygame.display.set_mode((ai_settings.screen_width,
                                               ai_settings.screen_height))
        self.ship = Ship(self.screen, self.settings)
        self.bullets = Group()
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        # 开始游戏主循环
        while True:
            # 监视键盘和鼠标事件
            gf.check_events(self.settings, self.screen, self.ship,
                            self.bullets)
            self.ship.update()
            gf.update_bullets(self.bullets)
            # 让最近绘制的屏幕可见
            gf.update_screen(self.settings, self.screen, self.ship,
                             self.bullets)


if __name__ == '__main__':
    ai_settings = Settings()
    new_game = Game(ai_settings)
    new_game.run_game()
