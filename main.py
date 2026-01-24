from game import Renderer, Player, Controller

class GameApp:
    def __init__(self, width: int, height: int):
        self.renderer = Renderer(width, height)
        self.player = Player(100, 100, 0.2, 'player.png')
        self.controller = Controller()

    def run(self):
        while self.renderer._running:
            self.renderer.clear()
            self.renderer.poll_events()

            action = self.controller.get_actions()
            self.player.apply_actions(action)

            self.renderer.draw_player(self.player)
            self.renderer.present()

        self.renderer.quit()


GameApp(800, 600).run()