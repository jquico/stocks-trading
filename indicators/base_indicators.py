import talib
import pandas as pd

def calculate_rsi(df, period=14):
    """
    Calcula o índice de força relativa (RSI) para os preços de fechamento.
    :param df: DataFrame com dados históricos da ação
    :param period: Período para o cálculo do RSI (geralmente 14 dias)
    :return: DataFrame com a coluna 'RSI'
    """
    df['RSI'] = talib.RSI(df['Close'], timeperiod=period)
    return df

def calculate_macd(df, fastperiod=12, slowperiod=26, signalperiod=9):
    """
    Calcula o MACD (Moving Average Convergence Divergence) e sua linha de sinal.
    :param df: DataFrame com dados históricos da ação
    :param fastperiod: Período para a média exponencial rápida
    :param slowperiod: Período para a média exponencial lenta
    :param signalperiod: Período para a linha de sinal
    :return: DataFrame com as colunas 'MACD' e 'MACD_signal'
    """
    macd, macd_signal, _ = talib.MACD(df['Close'], fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
    df['MACD'] = macd
    df['MACD_signal'] = macd_signal
    return df

def calculate_sma(df, period=50):
    """
    Calcula a média móvel simples (SMA).
    :param df: DataFrame com dados históricos da ação
    :param period: Período para o cálculo da média móvel simples
    :return: DataFrame com a coluna 'SMA'
    """
    df['SMA'] = talib.SMA(df['Close'], timeperiod=period)
    return df

def calculate_ema(df, period=50):
    """
    Calcula a média móvel exponencial (EMA).
    :param df: DataFrame com dados históricos da ação
    :param period: Período para o cálculo da média móvel exponencial
    :return: DataFrame com a coluna 'EMA'
    """
    df['EMA'] = talib.EMA(df['Close'], timeperiod=period)
    return df

def calculate_stochastic_oscillator(df, fastk_period=14, fastd_period=3):
    """
    Calcula o oscilador estocástico (Stochastic Oscillator).
    :param df: DataFrame com dados históricos da ação
    :param fastk_period: Período para o cálculo do %K
    :param fastd_period: Período para o cálculo do %D
    :return: DataFrame com as colunas '%K' e '%D'
    """
    slowk, slowd = talib.STOCH(df['High'], df['Low'], df['Close'], fastk_period=fastk_period, fastd_period=fastd_period)
    df['%K'] = slowk
    df['%D'] = slowd
    return df

def calculate_adx(df, period=14):
    """
    Calcula o Índice de Direção Média (ADX).
    :param df: DataFrame com dados históricos da ação
    :param period: Período para o cálculo do ADX
    :return: DataFrame com a coluna 'ADX'
    """
    df['ADX'] = talib.ADX(df['High'], df['Low'], df['Close'], timeperiod=period)
    return df

def main():
    # Example usage
    ticker = 'AAPL'  # Ticker da ação
    data = pd.read_csv(f"data/stocks/{ticker}_historical_data.csv")
    
    # Calculando RSI
    data = calculate_rsi(data)
    print("RSI calculado.")
    
    # Calculando MACD
    data = calculate_macd(data)
    print("MACD calculado.")
    
    # Calculando SMA
    data = calculate_sma(data)
    print("SMA calculada.")
    
    # Calculando EMA
    data = calculate_ema(data)
    print("EMA calculada.")
    
    # Calculando Stochastic Oscillator
    data = calculate_stochastic_oscillator(data)
    print("Oscilador Estocástico calculado.")
    
    # Calculando ADX
    data = calculate_adx(data)
    print("ADX calculado.")
    
    # Display the first few rows to check results
    print(data.head())

if __name__ == "__main__":
    main()
