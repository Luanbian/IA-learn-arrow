from ..physics.adapter.physics_adapter import PhysicsProjectileAdapter

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