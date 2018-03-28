import sys

import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 相应按键
        elif event.type == pygame.KEYDOWN:  # 相应不断移动
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            # 限制屏幕上子弹数量
            elif event.key == pygame.K_SPACE and len(
                    bullets) < ai_settings.bullet_allowed:
                new_bullet = Bullet(ai_settings, screen, ship)
                bullets.add(new_bullet)
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            # elif event.type == pygame.K_SPACE:
            #     new_bullet = Bullet(ai_settings, screen, ship)
            #     bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    # 更新子弹
    bullets.update()
    # 如果子弹溢出显示区域，则删除它
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def creat_fleet(ai_settings, screen, aliens):
    # 创建外星人群
    alien = Alien(ai_settings, screen)
    # 计算一行可容纳多少外星人
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # 创建一行外星人
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        # 每2个外星人间隔一个宽度
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
