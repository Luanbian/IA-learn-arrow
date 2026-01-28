import math

class Player:
    def __init__(self, pos: tuple, speed: int, image: str, factory):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.speed = speed
        self.speed_y = 0.0
        self.angle = 45
        self.power = 600
        self.image = f"assets/{image}"
        self.isShooting = False
        self.factory = factory
        
    def apply_actions(self, action: dict):
        self.pos_x += action.get("x", 0) * self.speed
        self.pos_y += action.get("y", 0) * self.speed
        self.rotate(action.get("rotate", 0))
        self.change_power(action.get("power", 0))
        self.isShooting = action.get("shoot", False)

    def rotate(self, delta):
        self.angle = max(5, min(85, self.angle + delta))

    def change_power(self, delta):
        self.power = max(100, min(1200, self.power + delta))
    
    def shoot(self):
        if not self.isShooting:
            return

        angle_rad = math.radians(self.angle)

        velocity_x = self.power * math.cos(angle_rad)
        velocity_y = -self.power * math.sin(angle_rad)

        self.factory.create((self.pos_x, self.pos_y), (velocity_x, velocity_y))

        self.isShooting = False