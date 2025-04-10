# Script principal de teste do bot
import pandas as pd
import ta
import yfinance as yf
from stable_baselines3 import PPO
from env.trading_env import TradingEnv
from stable_baselines3.common.vec_env import DummyVecEnv

def load_test_data(symbol="AAPL", start="2024-01-01", end="2024-12-31"):
    df = yf.download(symbol, start=start, end=end)
    df.dropna(inplace=True)

    df['rsi'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    macd = ta.trend.MACD(df['Close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    df['sma_10'] = ta.trend.SMAIndicator(df['Close'], window=10).sma_indicator()
    df['sma_50'] = ta.trend.SMAIndicator(df['Close'], window=50).sma_indicator()
    df['atr'] = ta.volatility.AverageTrueRange(df['High'], df['Low'], df['Close']).average_true_range()
    df['obv'] = ta.volume.OnBalanceVolumeIndicator(df['Close'], df['Volume']).on_balance_volume()

    return df.dropna()

def test_model():
    model = PPO.load("models/ppo_trading_bot")
    test_df = load_test_data()
    env = DummyVecEnv([lambda: TradingEnv(test_df)])

    obs = env.reset()
    done = False
    total_reward = 0

    while not done:
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)
        total_reward += reward[0]

    print(f"✅ Teste concluído — Lucro total estimado: ${total_reward:.2f}")

if __name__ == "__main__":
    test_model()
