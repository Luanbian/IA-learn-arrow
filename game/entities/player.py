import math

class Player:
    def __init__(self, pos: tuple, speed: int, image: str):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.speed = speed
        self.speed_y = 0.0
        self.angle = 45
        self.power = 600
        self.image = f"assets/{image}"
        
    def apply_actions(self, action: dict):
        self.pos_x += action.get("x", 0) * self.speed
        self.pos_y += action.get("y", 0) * self.speed

    def rotate(self, delta):
        self.angle = max(5, min(85, self.angle + delta))

    def change_power(self, delta):
        self.power = max(100, min(1200, self.power + delta))