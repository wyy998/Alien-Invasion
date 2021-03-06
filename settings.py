import os


class Settings():
    # 存储《外星人入侵》游戏的所有设置的类
    def __init__(self):
        # 资源路径，windows不能直接使用相对路径
        self.path = os.path.abspath('.') + '/images/'
        # 屏幕设置
        self.caption = 'Alien Invasion'
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0xff, 0xfa, 0xfa)
        # 飞船速度
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0xff, 0x8c, 0x00)
        self.bullet_allowed = 3
