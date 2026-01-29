from game.render.renderer import Renderer
from game.controllers.controller import Controller
from game.world import GameWorld
from constants.environment import SCREEN_WIDTH, SCREEN_HEIGHT

class GameApp:
    def __init__(self):
        self.renderer = Renderer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.controller = Controller()
        self.world = GameWorld()

    def run(self):
        while True:
            delta = self.renderer.get_time()
            action = self.controller.get_actions()

            self.world.step(delta, action)

            self.render()

    def render(self):
        self.renderer.clear()
        self.renderer.draw_terrain()

        player = self.world.player
        self.renderer.draw_player(player)

        for projectile, _ in self.world.projectile_factory.projectiles:
            self.renderer.draw_projectile(projectile)

        for reward, _ in self.world.reward_factory.rewards:
            self.renderer.draw_reward(reward)

        self.renderer.draw_info(
            player.angle,
            player.power,
            player.points
        )

        self.renderer.present()

GameApp().run()