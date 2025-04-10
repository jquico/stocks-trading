# Integração com Alpaca API
import alpaca_trade_api as tradeapi
import os

class AlpacaConnector:
    def __init__(self, api_key=None, api_secret=None, base_url="https://paper-api.alpaca.markets"):
        """Initializes the Alpaca API connection."""
        self.api_key = api_key or os.getenv('ALPACA_API_KEY')
        self.api_secret = api_secret or os.getenv('ALPACA_API_SECRET')
        self.base_url = base_url
        
        # Initialize the Alpaca API client
        self.api = tradeapi.REST(self.api_key, self.api_secret, self.base_url, api_version='v2')

    def get_account_info(self):
        """Retrieves account information."""
        try:
            account = self.api.get_account()
            return account
        except Exception as e:
            print(f"Error retrieving account information: {e}")
            return None

    def get_market_data(self, symbol, timeframe="day", limit=100):
        """Retrieves historical market data for a specific symbol."""
        try:
            barset = self.api.get_barset(symbol, timeframe, limit=limit)
            data = barset[symbol]
            return data
        except Exception as e:
            print(f"Error retrieving market data: {e}")
            return None

    def place_order(self, symbol, qty, side, type="market", time_in_force="gtc"):
        """Places an order (buy/sell) with Alpaca."""
        try:
            order = self.api.submit_order(
                symbol=symbol,
                qty=qty,
                side=side,
                type=type,
                time_in_force=time_in_force
            )
            return order
        except Exception as e:
            print(f"Error placing order: {e}")
            return None

    def get_order_status(self, order_id):
        """Retrieves the status of a specific order."""
        try:
            order = self.api.get_order(order_id)
            return order
        except Exception as e:
            print(f"Error retrieving order status: {e}")
            return None

    def list_open_orders(self):
        """Lists all open orders."""
        try:
            orders = self.api.list_orders(status='open')
            return orders
        except Exception as e:
            print(f"Error retrieving open orders: {e}")
            return []

    def cancel_order(self, order_id):
        """Cancels a specific order."""
        try:
            self.api.cancel_order(order_id)
            print(f"Order {order_id} has been canceled.")
        except Exception as e:
            print(f"Error canceling order: {e}")

    def get_position(self, symbol):
        """Retrieves the position (stocks owned) for a specific symbol."""
        try:
            position = self.api.get_account().cash
            return position
        except Exception as e:
            print(f"Error retrieving position for {symbol}: {e}")
            return None
