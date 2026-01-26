import pygame
from ..entities.player import Player
from constants.environment import (FPS, SCREEN_WIDTH, SCREEN_HEIGHT,TERRAIN_HEIGHT)

class Renderer:
    def __init__(self, width: int, height: int):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
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
    
    def draw_terrain(self):
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(0, SCREEN_HEIGHT - TERRAIN_HEIGHT, SCREEN_WIDTH, TERRAIN_HEIGHT))
        
    def present(self):
        pygame.display.flip()
    
    def clear(self):
        self.screen.fill((255, 255, 255))

    def get_time(self):
        return self.clock.tick(FPS) / 1000.0