from typing import Protocol

class PhysicalBody(Protocol):
    pos_x: float
    pos_y: float
    speed: float
    speed_y: float