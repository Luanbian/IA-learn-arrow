from constants.environment import PLAYER_ASSET, PLAYER_SPEED, PLAYER_START_POS, TERRAIN_HEIGHT
from game.entities.player import Player
from game.entities.terrain import Terrain
from game.entities.projectile import ProjectileFactory
from game.entities.reward import RewardFactory
from game.physics.physics import Physics
from game.rules import GameRules

class GameWorld:
    def __init__(self):
        self.physics = Physics()
        self.projectile_factory = ProjectileFactory(self.physics)
        self.reward_factory = RewardFactory(self.physics)

        self.player = Player(
            PLAYER_START_POS,
            PLAYER_SPEED,
            PLAYER_ASSET,
            self.projectile_factory,
            self.physics
        )

        self.terrain = Terrain(TERRAIN_HEIGHT, self.physics)

        self.player.create()
        self.terrain.create()
        self.reward_factory.create()

        self.rules = GameRules(self.player, self.reward_factory)

    def step(self, delta: float, action: dict | None = None):
        if action and any(action.values()):
            self.apply_action(action)

        self.physics.step(delta)

        self.player.sync_from_physics()

        for projectile, adapter in self.projectile_factory.projectiles:
            adapter.sync_to_entity(projectile)

        reward = 0.0
        for event in self.physics.consume_events():
            reward += self.rules.handle_events(event)

        return reward

    def apply_action(self, action):
        body = self.player.physics_body_adapter.body

        move = action.get("x", 0)
        if move != 0:
            force = (move * PLAYER_SPEED * 50, 0)
            body.apply_force_at_local_point(force)

        if action.get("shoot"):
            self.player.shoot()


