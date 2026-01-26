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
        self.isShooting = False
        
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
    
    def shoot(self, projectile):
        if not self.isShooting:
            return

        angle_rad = math.radians(self.angle)

        velocity_x = self.power * math.cos(angle_rad)
        velocity_y = -self.power * math.sin(angle_rad)

        projectile.body.position = (self.pos_x, self.pos_y)
        projectile.body.velocity = (velocity_x, velocity_y)

        self.isShooting = False

        