from game import Renderer, Player, Controller, Physics, Terrain, ProjectileFactory
from constants.environment import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    PLAYER_START_POS, PLAYER_SPEED,PLAYER_ASSET, TERRAIN_HEIGHT
)

class GameApp:
    def __init__(self):
        self.renderer = Renderer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.physics = Physics()
        self.controller = Controller()

        self.projectile_factory = ProjectileFactory(self.physics)

        self.player = Player(PLAYER_START_POS, PLAYER_SPEED, PLAYER_ASSET, self.projectile_factory, self.physics)
        self.player.create()
        self.terrain = Terrain(TERRAIN_HEIGHT, self.physics)
        self.terrain.create()

    def run(self):
        while True:
            delta = self.renderer.get_time()

            self.handle_events()
            self.apply_controller_actions()

            self.physics.step(delta)
            self.player.physics_body_adapter.sync_to_entity(self.player)

            for projectile, adapter in self.projectile_factory.projectiles[:]:
                adapter.sync_to_entity(projectile)
                adapter.apply_rolling_resistance()
                self.renderer.draw_projectile(projectile)
            
            self.projectile_factory.cleanUp()

            self.renderer.draw_terrain()
            self.renderer.draw_info(self.player.angle, self.player.power)
            self.render_player()

    def handle_events(self):
        self.renderer.clear()

    def apply_controller_actions(self):
        action = self.controller.get_actions()
        self.player.apply_actions(action)

        speed_x = action.get("x", 0) * PLAYER_SPEED
        cur_speed_y = self.player.physics_body_adapter.body.velocity.y

        self.player.physics_body_adapter.body.velocity = (speed_x, cur_speed_y)

        if action['shoot']:
            self.player.shoot()

    def render_player(self):
        self.renderer.draw_player(self.player)
        self.renderer.present()

GameApp().run()