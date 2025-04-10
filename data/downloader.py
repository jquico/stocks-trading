# Script para download e preparação de dados históricos
import yfinance as yf

def download_data(ticker, start_date="2010-01-01", end_date="2025-01-01"):
    """
    Função para baixar dados históricos de ações.
    :param ticker: Símbolo da ação (exemplo: 'AAPL' para Apple)
    :param start_date: Data de início para os dados históricos
    :param end_date: Data de término para os dados históricos
    :return: DataFrame com os dados históricos
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    return data
