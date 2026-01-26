import pymunk
from constants.environment import GRAVITY

class Physics:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = GRAVITY

    def add(self, adapter):
        self.space.add(adapter.body, adapter.shape)

    def step(self, dt: float):
        self.space.step(dt)