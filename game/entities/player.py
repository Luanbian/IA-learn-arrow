class Player:
    def __init__(self, pos: tuple, speed: int, image: str):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.speed = speed
        self.speed_y = 0.0
        self.image = f"assets/{image}"
        
    def apply_actions(self, action: dict):
        self.pos_x += action.get("x", 0) * self.speed
        self.pos_y += action.get("y", 0) * self.speed