from game import Renderer, Player, Controller, Physics, PhysicsAdapter
from game.environment import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    PLAYER_START_POS, PLAYER_MASS,
    PLAYER_SIZE, PLAYER_SPEED,PLAYER_ASSET
)

class GameApp:
    def __init__(self):
        self.renderer = Renderer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.physics = Physics()
        self.player = Player(PLAYER_START_POS, PLAYER_SPEED, PLAYER_ASSET)
        self.physics_adapter = PhysicsAdapter(
            mass=PLAYER_MASS,
            size=PLAYER_SIZE,
            position=PLAYER_START_POS
        )
        self.physics.add(self.physics_adapter)
        self.controller = Controller()

    def run(self):
        while self.renderer._running:
            delta = self.renderer.get_time()

            self.handle_events()
            self.render_player()
            self.apply_controller_actions()

            self.physics_adapter.sync_to_entity(self.player)
            self.physics.step(delta)

        self.renderer.quit();

    def handle_events(self):
        self.renderer.clear()
        self.renderer.poll_events()
    
    def apply_controller_actions(self):
        action = self.controller.get_actions()
        self.player.apply_actions(action)

    def render_player(self):
        self.renderer.draw_player(self.player)
        self.renderer.present()
    


GameApp().run()