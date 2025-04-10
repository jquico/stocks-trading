# Combinação heurísticas + DRL
import pandas as pd
from stable_baselines3 import PPO
from env.trading_env import TradingEnv
from stable_baselines3.common.vec_env import DummyVecEnv
from models.rule_based import sma_cross_strategy, rsi_strategy

class HybridBot:
    def __init__(self, model_path="models/ppo_trading_bot", df=None):
        self.model = PPO.load(model_path)
        self.df = df
        self.env = DummyVecEnv([lambda: TradingEnv(df)])
        self.obs = self.env.reset()

        # Geração dos sinais de estratégias simples
        self.rule_signals = self.generate_rule_signals(df)

    def generate_rule_signals(self, df):
        sma_signals = sma_cross_strategy(df)[["signal"]]
        rsi_signals = rsi_strategy(df)[["signal"]]
        combined = pd.concat([sma_signals, rsi_signals], axis=1).fillna(0)
        combined.columns = ["sma_signal", "rsi_signal"]
        combined["total_signal"] = combined.sum(axis=1)
        return combined["total_signal"].tolist()

    def decide_action(self, step):
        action, _ = self.model.predict(self.obs)

        # Obter sinal das regras no passo atual
        rule_signal = self.rule_signals[step]
        
        # Combinar decisão: regra tem mais peso se DRL está neutro
        if rule_signal == 1:
            action = 2  # Força compra
        elif rule_signal == -1:
            action = 0  # Força venda
        # Caso contrário, segue o DRL

        return action

    def run(self):
        done = False
        step = self.env.envs[0].current_step
        total_reward = 0

        while not done:
            action = self.decide_action(step)
            self.obs, reward, done, _ = self.env.step([action])
            total_reward += reward[0]
            step += 1

        print(f"🤖 Lucro total (Hybrid Bot): ${total_reward:.2f}")
