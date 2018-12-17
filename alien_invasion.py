# import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import  Alien
def run_game():
    pygame.init()
    ai_settings = Settings()
    # screen = pygame.display.set_mode((1200,800))
    # bg_color = (230,230,230)
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alienware Invasion")


    ship = Ship(ai_settings,screen)

    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # alien = Alien(ai_settings,screen)

    while True:
        ship.blitme()
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(aliens,bullets)
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        # print(len(bullets))
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        # screen.fill(ai_settings.bg_color)
        # pygame.display.flip()


run_game()

