import pygame

class Controller:
    def get_actions(self) -> dict:
        keys = pygame.key.get_pressed()

        actions = {"x": 0, "y": 0}

        if keys[pygame.K_LEFT]:
            actions["x"] = -1
        if keys[pygame.K_RIGHT]:
            actions["x"] = 1
        if keys[pygame.K_UP]:
            actions["y"] = -1
        if keys[pygame.K_DOWN]:
            actions["y"] = 1
            
        return actions