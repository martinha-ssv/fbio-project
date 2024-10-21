import pygame
import sys
import time
import logging
import constants as gc # import game.constants as gc # 
from sprites import SpriteObject # from game.sprites import SpriteObject # 
from player import Player # from game.player import Player #


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class Game():
    def __init__(self):#, data):
        logger.debug('Inside init')
        #self.data = data
        self.running = True
        self.player_count = 0
        pygame.init()
        self.window = pygame.display.set_mode((gc.WIDTH, gc.HEIGHT))


        # PHYSICAL CONSTANTS
        self.Lw = 1.0  # Left weight (kg)
        self.Rw = 1.0 # Right weight (kg)
                
   




    def run(self):
        # TODO when w is pressed, enter menu to change weights

        
        self.clock = pygame.time.Clock()
        logger.debug('Started running')

        spacing = 0 if self.player_count == 1 else (gc.WIDTH - 2*gc.safe_margin_x) / (self.player_count - 1)
        for i in range(self.player_count):
            center_line = gc.WIDTH//2 if self.player_count == 1 else gc.safe_margin_x + spacing*i 
            logger.debug(f'Creating player {i}\n >> center_line: {center_line}')
            Player(f'Player {i}', self.window, center_line)


        while self.running:
            self.window.fill(gc.PURPLE)
            for player in Player.players:
                player.draw()
                #player.updateWeights(1,1)

            pygame.display.flip()
            
            self.clock.tick(gc.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KSCAN_LEFT:
                    self.signal = -1
                if event.type == pygame.KSCAN_RIGHT:
                    self.signal = 1

    def startMenu(self, screen):
        # Define text for the start menu
        font = pygame.font.SysFont(None, 50)

        start_text = font.render('Start Game', True, gc.WHITE)
        quit_text = font.render('Quit Game', True, gc.WHITE)

        # Create menu positions
        start_rect = start_text.get_rect(center=(400, 250))
        quit_rect = quit_text.get_rect(center=(400, 350))
        player_count_text = font.render(f'Players: {self.player_count}', True, gc.WHITE)
        player_count_rect = player_count_text.get_rect(center=(400, 150))
        
        while True:
            # Fill the screen with a color (background)
            screen.fill(gc.BLACK)

            # Draw the text on the screen
            screen.blit(start_text, start_rect)
            screen.blit(quit_text, quit_rect)
            player_count_text = font.render(f'Players: {self.player_count}', True, gc.WHITE)
            screen.blit(player_count_text, player_count_rect)


            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_rect.collidepoint(event.pos):
                        # Start the game
                        return
                    elif quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # Increase player count but not above the max limit
                        if self.player_count < gc.max_players:
                            self.player_count += 1

                    if event.key == pygame.K_DOWN:
                        # Decrease player count but not below 1
                        if self.player_count > 1:
                            self.player_count -= 1


            # Update the screen
            pygame.display.update()
            
game = Game()
game.startMenu(game.window)
game.run()
