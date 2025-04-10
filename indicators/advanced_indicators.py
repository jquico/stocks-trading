import talib
import pandas as pd
from sklearn.decomposition import PCA

def calculate_bollinger_bands(df, time_period=20, nbdevup=2, nbdevdn=2):
    """
    Função para calcular as Bandas de Bollinger.
    :param df: DataFrame com os dados históricos da ação
    :param time_period: Período para calcular as bandas
    :param nbdevup: Número de desvios padrão para a banda superior
    :param nbdevdn: Número de desvios padrão para a banda inferior
    :return: DataFrame com as bandas superior, média e inferior
    """
    upperband, middleband, lowerband = talib.BBANDS(df['Close'], timeperiod=time_period, nbdevup=nbdevup, nbdevdn=nbdevdn)
    df['Bollinger_upper'] = upperband
    df['Bollinger_middle'] = middleband
    df['Bollinger_lower'] = lowerband
    return df

def calculate_atr(df, time_period=14):
    """
    Função para calcular o Índice de Volatilidade (ATR).
    :param df: DataFrame com os dados históricos da ação
    :param time_period: Período para calcular o ATR
    :return: DataFrame com a coluna ATR
    """
    atr = talib.ATR(df['High'], df['Low'], df['Close'], timeperiod=time_period)
    df['ATR'] = atr
    return df

def calculate_obv(df):
    """
    Função para calcular o On-Balance Volume (OBV).
    :param df: DataFrame com os dados históricos da ação
    :return: DataFrame com a coluna OBV
    """
    obv = talib.OBV(df['Close'], df['Volume'])
    df['OBV'] = obv
    return df

def calculate_pca(df, n_components=2):
    """
    Função para realizar PCA (Análise de Componentes Principais) nos preços históricos.
    :param df: DataFrame com os dados históricos da ação
    :param n_components: Número de componentes principais
    :return: DataFrame com os componentes principais
    """
    pca = PCA(n_components=n_components)
    df_pca = df[['Open', 'High', 'Low', 'Close']].dropna()
    pca_result = pca.fit_transform(df_pca)
    
    for i in range(n_components):
        df[f'PCA_{i+1}'] = pca_result[:, i]
    
    return df

def main():
    # Example usage
    ticker = 'AAPL'  # Ticker da ação
    data = pd.read_csv(f"data/stocks/{ticker}_historical_data.csv")
    
    # Calculando Bandas de Bollinger
    data = calculate_bollinger_bands(data)
    print("Bandas de Bollinger calculadas.")
    
    # Calculando ATR
    data = calculate_atr(data)
    print("ATR calculado.")
    
    # Calculando OBV
    data = calculate_obv(data)
    print("OBV calculado.")
    
    # Calculando PCA
    data = calculate_pca(data)
    print("PCA calculado.")
    
    # Display the first few rows to check results
    print(data.head())

if __name__ == "__main__":
    main()
