from .physics_types import PhysicalBody

class Physics:
    def __init__(self):
        self.gravity = 9.81

    def apply_gravity(self, body: PhysicalBody, time: float):
        body.speed_y += self.gravity * time
        body.pos_y += body.speed_y * time