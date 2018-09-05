import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np

class PickerEnv(gym.Env):

    def __init__(self):
        self.state = np.random.random((128,128,3))
        self.viewer = None
        self._action_space = None
        pass

    @property
    def action_space(self):
        return self._action_space

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        pass
        reward = 1
        done = False
        return np.array(self.state), reward, done, {}

    def reset(self):
        pass
        return np.array(self.state)

    def render(self, mode='human', close=False):
        if close and self.viewer:
            self.viewer.close()
            self.viewer = None
            return

        img = self.state
        if mode == 'rgb_array':
            return img
        elif mode == 'human':
            from gym.envs.classic_control import rendering
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)

    def close(self):
        pass