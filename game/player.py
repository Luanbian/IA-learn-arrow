class Player:
    def __init__(self, pos_x: int, pos_y: int, speed: int, image: str):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.image = f"assets/{image}"
        
    def apply_actions(self, action: dict):
        self.pos_x += action.get("x", 0) * self.speed
        self.pos_y += action.get("y", 0) * self.speed