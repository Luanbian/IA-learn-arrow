from game.events import GameEventType

class GameRules:
    def __init__(self, player, reward_factory):
        self.player = player
        self.reward_factory = reward_factory
        
    def handle_events(self, event):
        if event.type == GameEventType.PROJECTILE_HIT_REWARD:
            self.player.earn_point()
            self.reward_factory.create()
            return 1.0
        return 0.0