import pymunk
from constants.environment import REWARD_COLLISION, PROJECTILE_COLLISION

class PhysicsBodyAdapter:
    def __init__(self, mass: float, size: tuple[int, int], position: tuple[float, float]):
        moment = pymunk.moment_for_box(mass, size)
        self.body = pymunk.Body(mass, moment)
        self.body.position = position

        self.shape = pymunk.Poly.create_box(self.body, size)
        self.shape.friction = 1.5
        self.shape.elasticity = 0.0

    def sync_to_entity(self, entity):
        entity.pos_x = self.body.position.x
        entity.pos_y = self.body.position.y

class PhysicsTerrainAdapter:
   def __init__(self, pos_y: float, width: float, height: float):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = (width / 2, pos_y)

        self.shape = pymunk.Poly.create_box(self.body, (width, height))
        self.shape.elasticity = 0.0
        self.shape.friction = 1.0

class PhysicsProjectileAdapter:
    def __init__(self, mass: float, radius: float, position: tuple[float, float]):
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, moment)
        self.shape = pymunk.Circle(self.body, radius)
        self.body.position = position
        self.body.damping = 0.999
        self.body.angular_damping = 0.9
        self.shape.friction = 1.5
        self.shape.elasticity = 0.0
        self.shape.collision_type = PROJECTILE_COLLISION

    def sync_to_entity(self, entity):
        entity.pos_x = self.body.position.x
        entity.pos_y = self.body.position.y
    
    def apply_rolling_resistance(self):
        (vx, vy) = self.body.velocity

        if abs(vy) == 0:
            self.body.velocity = (0, vy)
        else:
            self.body.velocity = (vx * 0.99, vy)

class PhysicsRewardAdapter:
    def __init__(self, position: tuple[float, float], radius: float):
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position = position

        self.shape = pymunk.Circle(self.body, radius)

        self.shape.elasticity = 0.9
        self.shape.friction = 0.5
        self.shape.collision_type = REWARD_COLLISION