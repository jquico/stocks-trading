import pandas as pd

def calculate_return(df):
    """
    Calcula o retorno total baseado nos preços de fechamento.
    :param df: DataFrame com os dados históricos da ação
    :return: Retorno total
    """
    return (df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0]

def calculate_drawdown(df):
    """
    Calcula o drawdown máximo, que é a maior queda em relação ao pico.
    :param df: DataFrame com os dados históricos da ação
    :return: Drawdown máximo
    """
    peak = df['Close'].cummax()
    drawdown = (df['Close'] - peak) / peak
    return drawdown.min()
