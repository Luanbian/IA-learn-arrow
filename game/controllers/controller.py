import pygame

class Controller:
    def get_actions(self) -> dict:
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        actions = {"x": 0, "rotate": 0, "power": 0, "shoot": False}

        if keys[pygame.K_LEFT]:
            actions["x"] = -1
        if keys[pygame.K_RIGHT]:
            actions["x"] = 1
        if keys[pygame.K_UP]:
            actions["rotate"] += 1
        if keys[pygame.K_DOWN]:
            actions["rotate"] -= 1
        if keys[pygame.K_w]:
            actions["power"] += 10
        if keys[pygame.K_s]:
            actions["power"] -= 10
        if keys[pygame.K_SPACE]:
            actions["shoot"] = True

        return actions