import pymunk
from constants.environment import GRAVITY, PROJECTILE_COLLISION, REWARD_COLLISION
from game.events import GameEvent, GameEventType

class Physics:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = GRAVITY
        self.space.damping = 0.999
        self.space.sleep_time_threshold = 0.5
        self.space.idle_speed_threshold = 5
        self.space.on_collision(PROJECTILE_COLLISION, REWARD_COLLISION, begin=self.on_hit)
        self.events = []

    def add(self, adapter):
        self.space.add(adapter.body, adapter.shape)

    def remove(self, adapter):
        self.space.remove(adapter.body, adapter.shape)

    def step(self, dt: float):
        self.space.step(dt)
    
    def on_hit(self, arbiter, space, data):
        self.events.append(GameEvent(GameEventType.PROJECTILE_HIT_REWARD))
        return False

    def consume_events(self):
        events = self.events[:]
        self.events.clear()
        return events
