# Gráficos e visualizações
import matplotlib.pyplot as plt

def plot_candlestick_chart(df):
    """
    Função para gerar um gráfico de candlestick.
    :param df: DataFrame com dados históricos
    """
    import mplfinance as mpf
    mpf.plot(df, type='candle', style='charles', title="Candlestick Chart", ylabel='Preço de Fechamento')

def plot_rsi(df):
    """
    Função para gerar gráfico do RSI.
    :param df: DataFrame com dados históricos e o RSI calculado
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['RSI'], label='RSI', color='orange')
    plt.title('Índice de Força Relativa (RSI)')
    plt.legend()
    plt.show()
