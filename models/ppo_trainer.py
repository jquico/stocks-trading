# Treino PPO com Stable Baselines3
import pandas as pd
import yfinance as yf
import ta
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from env.trading_env import TradingEnv

def load_data(symbol="AAPL", start="2018-01-01", end="2023-12-31"):
    df = yf.download(symbol, start=start, end=end)
    df.dropna(inplace=True)

    # Indicadores técnicos
    df['rsi'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    macd = ta.trend.MACD(df['Close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    df['sma_10'] = ta.trend.SMAIndicator(df['Close'], window=10).sma_indicator()
    df['sma_50'] = ta.trend.SMAIndicator(df['Close'], window=50).sma_indicator()
    df['atr'] = ta.volatility.AverageTrueRange(df['High'], df['Low'], df['Close']).average_true_range()
    df['obv'] = ta.volume.OnBalanceVolumeIndicator(df['Close'], df['Volume']).on_balance_volume()

    df = df.dropna()
    return df

def train_model():
    df = load_data()
    env = DummyVecEnv([lambda: TradingEnv(df)])

    model = PPO(
        "MlpPolicy", env,
        learning_rate=3e-5,
        n_steps=2048,
        batch_size=64,
        gamma=0.99,
        ent_coef=0.005,
        clip_range=0.2,
        gae_lambda=0.95,
        verbose=1
    )

    model.learn(total_timesteps=50_000)
    model.save("models/ppo_trading_bot")
    print("✅ Modelo treinado e guardado em 'models/ppo_trading_bot'")

if __name__ == "__main__":
    train_model()
