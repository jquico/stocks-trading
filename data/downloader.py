import yfinance as yf
import os

def download_data(ticker, start_date="2010-01-01", end_date="2025-01-01"):
    """
    Função para baixar dados históricos de ações.
    :param ticker: Símbolo da ação (exemplo: 'AAPL' para Apple)
    :param start_date: Data de início para os dados históricos
    :param end_date: Data de término para os dados históricos
    :return: DataFrame com os dados históricos
    """
    try:
        # Baixando os dados históricos usando yfinance
        data = yf.download(ticker, start=start_date, end=end_date)
        print(f"Dados históricos para {ticker} baixados com sucesso!")
        return data
    except Exception as e:
        print(f"Erro ao baixar dados para {ticker}: {e}")
        return None

def save_data(data, ticker, file_path="data/stocks/"):
    """
    Função para salvar os dados históricos em um arquivo CSV.
    :param data: Dados históricos de ações
    :param ticker: Símbolo da ação
    :param file_path: Caminho para salvar o arquivo CSV
    :return: None
    """
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_name = f"{ticker}_historical_data.csv"
        data.to_csv(os.path.join(file_path, file_name))
        print(f"Dados de {ticker} salvos em {file_path}{file_name}")
    except Exception as e:
        print(f"Erro ao salvar dados para {ticker}: {e}")

def main():
    # Exemplo de uso
    ticker = 'AAPL'  # Ticker da ação (exemplo: 'AAPL' para Apple)
    data = download_data(ticker)
    if data is not None:
        save_data(data, ticker)

if __name__ == "__main__":
    main()
