from game import Renderer, Player, Controller, Physics, PhysicsAdapter

class GameApp:
    def __init__(self):
        self.renderer = Renderer(800, 600)
        self.physics = Physics()
        self.player = Player(100, 100, 0.2, 'player.png')
        self.physics_adapter = PhysicsAdapter(
            mass=1,
            size=(40, 40),
            position=(400,100)
        )
        self.physics.add(self.physics_adapter)
        self.controller = Controller()

    def run(self):
        while self.renderer._running:
            self.renderer.clear()
            self.renderer.poll_events()

            action = self.controller.get_actions()
            self.player.apply_actions(action)

            self.physics.step(self.renderer.get_time())
            self.renderer.draw_player(self.player)
            self.physics_adapter.sync_to_entity(self.player)
            self.renderer.present()

        self.renderer.quit()


GameApp().run()