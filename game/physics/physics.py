import pymunk
from constants.environment import GRAVITY

class Physics:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = GRAVITY
        self.space.damping = 0.999
        self.space.sleep_time_threshold = 0.5
        self.space.idle_speed_threshold = 5

    def add(self, adapter):
        self.space.add(adapter.body, adapter.shape)

    def remove(self, adapter):
        self.space.remove(adapter.body, adapter.shape)

    def step(self, dt: float):
        self.space.step(dt)