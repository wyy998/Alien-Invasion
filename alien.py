import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite):
    # 外星人类

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载图像
        self.image = pygame.image.load(ai_settings.path + 'alien.bmp')
        self.rect = self.image.get_rect()
        # 每个外星人最初都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的精确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
