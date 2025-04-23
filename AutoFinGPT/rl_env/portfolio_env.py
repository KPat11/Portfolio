#coding out our "portfolio" environment to see how our model works in action
#since this is just an excercise I will only be using 3 assets for trading decisions if I wanted to make this at scale I would probably just connect it to my stock brokerage account
import gym
from gym import spaces
import numpy as np

class SimplePortfolioEnv(gym.Env):
    def __init__(self):
        self.num_assets = 3 
        self.prices = np.random.rand(100,self.num_assets) * 100
        self.cash = 1000
        self.holdings = np.zeros(self.num_assets)
        self.current_step = 0

        # 👇 Observation space = cash + holdings + current prices
        low_obs = np.array([0.0] + [0.0]*self.num_assets + [0.0]*self.num_assets, dtype=np.float32)
        high_obs = np.array([np.inf] + [np.inf]*self.num_assets + [np.inf]*self.num_assets, dtype=np.float32)
        self.observation_space = spaces.Box(low=low_obs, high=high_obs, dtype=np.float32)

        # 👇 Action space = buy/sell amount per asset (continuous)
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(self.num_assets,), dtype=np.float32)

    def reset(self):
        self.cash = 1000
        self.holdings = np.zeros(self.num_assets)
        self.current_step = 0
        return self._get_obs()
    
    def _get_obs(self):
        return np.concatenate(([self.cash], self.holdings, self.prices[self.current_step]))
    
    def step(self, action):
        prices = self.prices[self.current_step]
        self.holdings += action
        self.cash -= np.dot(prices, action)
        self.current_step += 1
        done = self.current_step >= 99 #Each step will be considered a day we will look at a run for 99 days
        reward = np.sum(self.holdings * prices) + self.cash
        return self._get_obs(), reward, done, {}
    
    def render(self):
        print(f"Step {self.current_step} | Cash: {self.cash} | Holdings: {self.holdings}") #formatting for terminal to track in real time
    

