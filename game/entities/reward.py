import random
from ..physics.adapter.physics_adapter import PhysicsRewardAdapter
from constants.environment import REWARD_POS_X, REWARD_POS_Y

class Reward:
    def __init__(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]

class RewardFactory:
    def __init__(self, physics):
        self.physics = physics
        self.rewards = []

    def create(self):
        pos = (
            random.randint(REWARD_POS_X[0], REWARD_POS_X[1]),
            random.randint(REWARD_POS_Y[0], REWARD_POS_Y[1])
        )
        reward = Reward(pos)

        adapter = PhysicsRewardAdapter(
            position=(pos[0], pos[1]),
            radius=20.0
        )
        self.physics.add(adapter)

        if len(self.rewards) == 0:
            self.rewards.append((reward, adapter))
        else:
            self.physics.remove(self.rewards[0][1])
            self.rewards[0] = (reward, adapter)

        return reward