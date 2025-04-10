import pandas as pd

def calculate_return(df):
    """
    Calcula o retorno total baseado nos preços de fechamento.
    :param df: DataFrame com os dados históricos da ação
    :return: Retorno total
    """
    try:
        # Calcula o retorno total com base nos preços de fechamento
        total_return = (df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0]
        return total_return
    except Exception as e:
        print(f"Erro ao calcular retorno: {e}")
        return None

def calculate_drawdown(df):
    """
    Calcula o drawdown máximo, que é a maior queda em relação ao pico.
    :param df: DataFrame com os dados históricos da ação
    :return: Drawdown máximo
    """
    try:
        # Calcula o drawdown máximo com base no pico acumulado
        peak = df['Close'].cummax()
        drawdown = (df['Close'] - peak) / peak
        max_drawdown = drawdown.min()
        return max_drawdown
    except Exception as e:
        print(f"Erro ao calcular drawdown: {e}")
        return None

def main():
    # Example usage
    ticker = 'AAPL'  # Ticker da ação
    data = pd.read_csv(f"data/stocks/{ticker}_historical_data.csv")
    
    # Calculando retorno total
    total_return = calculate_return(data)
    print(f"Retorno total para {ticker}: {total_return * 100:.2f}%")
    
    # Calculando drawdown máximo
    max_drawdown = calculate_drawdown(data)
    print(f"Drawdown máximo para {ticker}: {max_drawdown * 100:.2f}%")

if __name__ == "__main__":
    main()
