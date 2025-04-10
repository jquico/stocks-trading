# Bollinger, ATR, OBV, PCA...
import talib
import pandas as pd

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
