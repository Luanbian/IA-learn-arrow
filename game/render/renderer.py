import pygame
from constants.environment import (FPS, SCREEN_WIDTH, SCREEN_HEIGHT,TERRAIN_HEIGHT)

class Renderer:
    def __init__(self, width: int, height: int):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def draw_player(self, player):
        player_asset = pygame.image.load(player.image).convert()
        self.screen.blit(player_asset, (player.pos_x, player.pos_y))
    
    def draw_terrain(self):
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(0, SCREEN_HEIGHT - TERRAIN_HEIGHT, SCREEN_WIDTH, TERRAIN_HEIGHT))
    
    def draw_projectile(self, projectile):
        pygame.draw.circle(self.screen, (255, 0, 0), (int(projectile.pos_x), int(projectile.pos_y)), 10)
    
    def draw_info(self, angle, power):
        font = pygame.font.Font(None, 36)
        angle_text = font.render(f"Angle: {angle}", True, (255, 0, 0))
        power_text = font.render(f"Power: {power}", True, (255, 0, 0))
        self.screen.blit(angle_text, (10, 10))
        self.screen.blit(power_text, (10, 50))
        
    def present(self):
        pygame.display.flip()
    
    def clear(self):
        self.screen.fill((255, 255, 255))

    def get_time(self):
        return self.clock.tick(FPS) / 1000.0