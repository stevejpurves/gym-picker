import argparse

import gym
from picker_env import PickerEnv

env = PickerEnv()
env.reset()
for n in range(4000):
    env.render()
    env.step(env.action_space.sample())