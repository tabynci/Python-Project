import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

def run_game():
    #initialize game and create a screen object
    pygame.init()
    
    ai_settings=Settings()
   
    screen = pygame.display.set_mode((ai_settings.screen_width ,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # make a ship.
    ship = Ship(ai_settings,screen)

    #Make a group to store bullets in 
    bullets = Group()
    aliens= Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen,ship, aliens)

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen,stats,sb, play_button, ship,aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,bullets)
            gf.update_aliens(ai_settings, stats,sb,screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen,stats,sb, ship,aliens, bullets, play_button)
        

   
        # Redraw the screen during each pass through the 
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
  

run_game()
