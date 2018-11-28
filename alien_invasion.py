# import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    # screen = pygame.display.set_mode((1200,800))
    # bg_color = (230,230,230)
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alienware Invasion")


    ship = Ship(ai_settings,screen)
    while True:
        ship.blitme()
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
        # screen.fill(ai_settings.bg_color)
        # pygame.display.flip()


run_game()

