from game import Renderer

class GameApp:
    def __init__(self, width: int, height: int):
        self.renderer = Renderer(width, height)

    def run(self):
        running = True
        while running:
            running = self.renderer.poll_events()

        self.renderer.quit()


app = GameApp(800, 600)
app.run()