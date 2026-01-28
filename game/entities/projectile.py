from ..physics.adapter.physics_adapter import PhysicsProjectileAdapter
from constants.environment import SCREEN_WIDTH

class Projectile:
    def __init__(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]

class ProjectileFactory:
    def __init__(self, physics):
        self.physics = physics
        self.projectiles = []

    def create(self, pos, velocity):
        projectile = Projectile(pos)

        adapter = PhysicsProjectileAdapter(
            mass=1,
            radius=8,
            position=pos,
            velocity=velocity
        )

        self.physics.add(adapter)
        self.projectiles.append((projectile, adapter))

        return projectile

    def cleanUp(self):
        for projectile, adapter in self.projectiles[:]:
            if adapter.body.position.x > SCREEN_WIDTH or adapter.body.position.x < 0:
                self.physics.remove(adapter)
                self.projectiles.remove((projectile, adapter))
