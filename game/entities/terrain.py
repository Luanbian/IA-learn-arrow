from constants.environment import SCREEN_HEIGHT, SCREEN_WIDTH
from ..physics.adapter.physics_adapter import PhysicsTerrainAdapter

class Terrain:
    def __init__(self, height: int, physics):
        self.height = height
        self.physics = physics
    
    def create(self):
        self.physics_terrain_adapter = PhysicsTerrainAdapter(
            pos_y=SCREEN_HEIGHT - self.height / 2,
            width=SCREEN_WIDTH * 2,
            height=self.height
        )
        self.physics.add(self.physics_terrain_adapter)