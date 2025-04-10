# Executa o bot em tempo real com corretora
import time
from datetime import datetime
from models.hybrid_model import HybridBot
from models.ppo_trainer import load_data

# Simula API
class BrokerAPI:
    def __init__(self, ticker):
        self.ticker = ticker
        self.cash = 10_000
        self.position = 0

    def get_latest_price(self):
        import yfinance as yf
        data = yf.download(self.ticker, period="1d", interval="1m")
        return data['Close'].iloc[-1]

    def submit_order(self, action, qty):
        price = self.get_latest_price()
        if action == "BUY":
            if self.cash >= price * qty:
                self.cash -= price * qty
                self.position += qty
                print(f"[{datetime.now()}] 📈 BUY {qty} @ {price:.2f}")
        elif action == "SELL":
            if self.position >= qty:
                self.cash += price * qty
                self.position -= qty
                print(f"[{datetime.now()}] 📉 SELL {qty} @ {price:.2f}")

    def portfolio_status(self):
        price = self.get_latest_price()
        value = self.cash + self.position * price
        return {
            "cash": self.cash,
            "position": self.position,
            "latest_price": price,
            "total_value": value
        }

def run_live_trading():
    ticker = "AAPL"
    df = load_data(ticker)
    bot = HybridBot(df=df)
    broker = BrokerAPI(ticker)

    step = bot.env.envs[0].current_step

    while True:
        action = bot.decide_action(step)
        price = broker.get_latest_price()

        if action == 2:
            broker.submit_order("BUY", qty=1)
        elif action == 0:
            broker.submit_order("SELL", qty=1)

        portfolio = broker.portfolio_status()
        print(f"💼 Portfolio: {portfolio}")
        time.sleep(60)  # 1 minuto

        step += 1
        if step >= len(df):
            print("⚠️ Fim dos dados históricos. Reiniciar ou carregar novos.")
            break

if __name__ == "__main__":
    run_live_trading()
