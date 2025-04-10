import os

BASE_DIR = "./"

STRUCTURE = [
    "data/stocks",
    "indicators",
    "env",
    "models",
    "evaluation",
    "brokers",
    "utils",
    "notebooks"
]

FILES = {
    "data/downloader.py": "# Script para download e preparação de dados históricos\n",
    "indicators/base_indicators.py": "# RSI, MACD, SMA...\n",
    "indicators/advanced_indicators.py": "# Bollinger, ATR, OBV, PCA...\n",
    "env/trading_env.py": "# Ambiente personalizado (gym.Env)\n",
    "models/ppo_trainer.py": "# Treino PPO com Stable Baselines3\n",
    "models/rule_based.py": "# Estratégias simples baseadas em regras\n",
    "models/hybrid_model.py": "# Combinação heurísticas + DRL\n",
    "evaluation/metrics.py": "# Sharpe Ratio, Drawdown, Profit Factor...\n",
    "evaluation/backtest.py": "# Script para backtesting com visualização\n",
    "brokers/alpaca_connector.py": "# Integração com Alpaca API\n",
    "utils/config.py": "# Parâmetros globais do projeto\n",
    "utils/visualizer.py": "# Gráficos e visualizações\n",
    "notebooks/explora_features.ipynb": "",
    "train.py": "# Script principal de treino do bot\n",
    "test.py": "# Script principal de teste do bot\n",
    "run_live.py": "# Executa o bot em tempo real com corretora\n",
    "requirements.txt": "pandas\nnumpy\nta\nyfinance\nmatplotlib\ngym\nstable-baselines3\nalpaca-trade-api\nscikit-learn\n",
    "README.md": "# Trading Bot com DRL + Estratégias Clássicas\n"
}

def create_structure():
    for folder in STRUCTURE:
        path = os.path.join(BASE_DIR, folder)
        os.makedirs(path, exist_ok=True)
        print(f"✔ Criada pasta: {path}")

    for file_path, content in FILES.items():
        full_path = os.path.join(BASE_DIR, file_path)
        with open(full_path, "w") as f:
            f.write(content)
        print(f"📄 Criado ficheiro: {full_path}")

if __name__ == "__main__":
    create_structure()
    print("\n✅ Estrutura criada com sucesso dentro de /stockes/")
