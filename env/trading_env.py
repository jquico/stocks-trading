# Ambiente personalizado (gym.Env)
import gym
import numpy as np
from gym import spaces

class TradingEnv(gym.Env):
    def __init__(self, df, window_size=10, initial_balance=10000):
        super().__init__()
        self.df = df.reset_index(drop=True)
        self.window_size = window_size
        self.initial_balance = initial_balance
        self.action_space = spaces.Discrete(3)  # 0: Vender, 1: Manter, 2: Comprar

        # A observação é uma janela de candles com todos os indicadores
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf,
            shape=(self.window_size, self.df.shape[1]),
            dtype=np.float32
        )

    def reset(self):
        self.balance = self.initial_balance
        self.position = 0
        self.entry_price = 0
        self.total_profit = 0
        self.current_step = self.window_size
        return self._get_obs()

    def _get_obs(self):
        return self.df.iloc[self.current_step - self.window_size:self.current_step].values

    def step(self, action):
        done = False
        current_price = self.df.iloc[self.current_step]["Close"]
        reward = 0

        # Ações: 0 = vender, 1 = manter, 2 = comprar
        if action == 2 and self.position == 0:
            self.position = 1
            self.entry_price = current_price
        elif action == 0 and self.position == 1:
            profit = current_price - self.entry_price
            reward = profit
            self.total_profit += profit
            self.position = 0
        else:
            reward = -0.01  # Penalidade por ação inútil

        self.current_step += 1
        if self.current_step >= len(self.df):
            done = True

        obs = self._get_obs()
        return obs, reward, done, {}

    def render(self, mode='human'):
        print(f"Step: {self.current_step}, Total Profit: {self.total_profit:.2f}")
