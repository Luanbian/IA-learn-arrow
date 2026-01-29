import pygame

class Controller:
    def get_actions(self) -> dict:
        actions = {"x": 0, "rotate": 0, "power": 0, "shoot": False}
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    actions['shoot'] = True 
                if event.key == pygame.K_LEFT:
                    actions["x"] = -1
                if event.key == pygame.K_RIGHT:
                    actions["x"] = 1
                if event.key == pygame.K_UP:
                    actions["rotate"] += 1
                if event.key == pygame.K_DOWN:
                    actions["rotate"] -= 1
                if event.key == pygame.K_w:
                    actions["power"] += 10
                if event.key == pygame.K_s:
                    actions["power"] -= 10
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        return actions