# Estratégias simples baseadas em regras
import pandas as pd

def sma_cross_strategy(df, short_window=10, long_window=50):
    df = df.copy()
    df['sma_short'] = df['Close'].rolling(window=short_window).mean()
    df['sma_long'] = df['Close'].rolling(window=long_window).mean()
    df.dropna(inplace=True)

    df['signal'] = 0
    df.loc[df['sma_short'] > df['sma_long'], 'signal'] = 1
    df.loc[df['sma_short'] < df['sma_long'], 'signal'] = -1

    return df[['Close', 'sma_short', 'sma_long', 'signal']]

def rsi_strategy(df, lower=30, upper=70):
    df = df.copy()
    df['rsi'] = df['Close'].rolling(window=14).apply(
        lambda x: 100 - (100 / (1 + ((x.diff().clip(lower=0).sum()) / abs(x.diff().clip(upper=0).sum())))), raw=False
    )
    df.dropna(inplace=True)

    df['signal'] = 0
    df.loc[df['rsi'] < lower, 'signal'] = 1   # Comprar quando RSI < 30
    df.loc[df['rsi'] > upper, 'signal'] = -1  # Vender quando RSI > 70

    return df[['Close', 'rsi', 'signal']]

def macd_strategy(df):
    df = df.copy()
    ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
    df['macd'] = ema_12 - ema_26
    df['signal_line'] = df['macd'].ewm(span=9, adjust=False).mean()
    df.dropna(inplace=True)

    df['signal'] = 0
    df.loc[df['macd'] > df['signal_line'], 'signal'] = 1
    df.loc[df['macd'] < df['signal_line'], 'signal'] = -1

    return df[['Close', 'macd', 'signal_line', 'signal']]
