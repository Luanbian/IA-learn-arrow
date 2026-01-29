from enum import Enum, auto

class GameEventType(Enum):
    PROJECTILE_HIT_REWARD = auto()

class GameEvent:
    def __init__(self, type: GameEventType, payload: dict | None = None):
        self.type = type
        self.payload = payload or {}