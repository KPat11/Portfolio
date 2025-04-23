#using the Porfolio env as our gym, we use the reinforcement learning library PPO to train on our "portfolio"

from stable_baselines3 import PPO
from portfolio_env import SimplePortfolioEnv

env = SimplePortfolioEnv()
model = PPO("MlpPolicy", env, verbose=1) #will be using multi-level perceptron
model.learn(total_timesteps=10000) #Training for 10000 steps in portfolio environment
model.save("models/ppo_portfolio")
