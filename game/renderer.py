import pygame
from .player import Player

class Renderer:
    def __init__(self, width: int, height: int):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Game Renderer")
        self._running = True
    
    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
        return self._running

    def quit(self):
        pygame.quit()

    def draw_player(self, player: Player):
        player_asset = pygame.image.load(player.image).convert()
        self.screen.blit(player_asset, (player.pos_x, player.pos_y))
        
    def present(self):
        pygame.display.flip()