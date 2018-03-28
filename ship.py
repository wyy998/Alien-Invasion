import pygame


class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载图片
        self.image = pygame.image.load(ai_settings.path + 'ship.bmp')
        # 获取图像外接矩形
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 中心X坐标处于屏幕X中心
        self.rect.bottom = self.screen_rect.bottom  # 底部与屏幕底部对齐

        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        # if self.moving_up:
        #     self.rect.bottom -= 1
        # if self.moving_down:
        #     self.rect.bottom += 1
        self.rect.centerx = self.center
