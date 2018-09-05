import gym
from picker_env import PickerEnv

env = PickerEnv()
env.reset()
for n in range(1000):
    env.render()