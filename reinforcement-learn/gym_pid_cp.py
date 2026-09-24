# From - https://ethanr2000.medium.com/using-pid-to-cheat-an-openai-challenge-f17745226449

import gymnasium as gym
from matplotlib import pyplot as plt
env = gym.make("CartPole-v1", render_mode="human")
observation = env.reset()

Kp = 135
Ki = 96.5
Kd = 47.5

force = 0
integral = 0
for _ in range(1000):
  env.render()

  #observation, reward, done, info = env.step(force)
  observation, reward, terminated, truncated, info = env.step(force)
  done = terminated or truncated

  velocity = observation[1]
  angle = observation[2]
  angular_velocity = observation[3]

  integral = integral + angle

  F = Kp*(angle) + Kd*(angular_velocity) + Ki*(integral)

  force = 1 if F > 0 else 0
  if done:
    observation = env.reset()
    integral = 0
env.close()
