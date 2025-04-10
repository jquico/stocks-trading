# Script para backtesting com visualização
import pandas as pd
import matplotlib.pyplot as plt
from models.ppo_trainer import load_data
from models.hybrid_model import HybridBot

def backtest_bot(df):
    bot = HybridBot(df=df)
    env = bot.env
    obs = env.reset()
    done = False
    step = env.envs[0].current_step

    portfolio = []
    position = 0
    cash = 10000
    equity_curve = []

    while not done:
        price = df.iloc[step]['Close']
        action = bot.decide_action(step)

        # 0 = Sell, 1 = Hold, 2 = Buy
        if action == 2 and cash >= price:
            position += 1
            cash -= price
        elif action == 0 and position > 0:
            position -= 1
            cash += price

        total_value = cash + position * price
        equity_curve.append(total_value)
        portfolio.append((step, action, price, total_value))

        obs, reward, done, _ = env.step([action])
        step += 1
        if step >= len(df):
            break

    return portfolio, equity_curve

def plot_equity_curve(equity_curve):
    plt.figure(figsize=(10, 5))
    plt.plot(equity_curve)
    plt.title("📈 Evolução da Carteira")
    plt.xlabel("Passos")
    plt.ylabel("Valor Total ($)")
    plt.grid(True)
    plt.show()

def calculate_metrics(portfolio, equity_curve):
    df = pd.DataFrame(portfolio, columns=["step", "action", "price", "value"])
    returns = pd.Series(equity_curve).pct_change().dropna()

    total_profit = equity_curve[-1] - equity_curve[0]
    max_drawdown = (max(equity_curve) - min(equity_curve)) / max(equity_curve)
    sharpe = returns.mean() / returns.std() * (252 ** 0.5) if returns.std() != 0 else 0

    print("💰 Total Profit:", round(total_profit, 2))
    print("📉 Max Drawdown:", round(max_drawdown * 100, 2), "%")
    print("⚖️ Sharpe Ratio:", round(sharpe, 2))

if __name__ == "__main__":
    df = load_data()
    portfolio, curve = backtest_bot(df)
    plot_equity_curve(curve)
    calculate_metrics(portfolio, curve)
