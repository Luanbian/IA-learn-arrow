import pymunk

class PhysicsBodyAdapter:
    def __init__(self, mass: float, size: tuple[int, int], position: tuple[float, float]):
        moment = pymunk.moment_for_box(mass, size)
        self.body = pymunk.Body(mass, moment)
        self.body.position = position

        self.shape = pymunk.Poly.create_box(self.body, size)

    def sync_to_entity(self, entity):
        entity.pos_x = self.body.position.x
        entity.pos_y = self.body.position.y

class PhysicsTerrainAdapter:
   def __init__(self, pos_y: float, width: float, height: float):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = (0, pos_y)

        self.shape = pymunk.Poly.create_box(self.body, (width, height))

class PhysicsProjectileAdapter:
    def __init__(self, mass: float, radius: float, position: tuple[float, float], velocity: tuple[float, float]):
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, moment)
        self.body.position = position
        self.body.velocity = velocity

        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 0.6
        self.shape.friction = 0.5

    def sync_to_entity(self, entity):
        entity.pos_x = self.body.position.x
        entity.pos_y = self.body.position.y