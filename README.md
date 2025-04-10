# Trading Bot – Projeto de Trading Automatizado

Este projeto visa criar um trading bot utilizando técnicas avançadas de **Deep Reinforcement Learning (DRL)** combinadas com **estratégias clássicas** de trading (como médias móveis, RSI, MACD, etc.), com o objetivo de maximizar lucros e minimizar riscos. O bot é treinado e testado com dados históricos e pode ser implementado em tempo real em corretoras (papel trading).

## Estrutura do Projeto

```
├── automate.py
├── brokers
│   └── alpaca_connector.py
├── create.py
├── data
│   ├── downloader.py
│   └── stocks
├── env
│   └── trading_env.py
├── evaluation
│   ├── backtest.py
│   └── metrics.py
├── indicators
│   ├── advanced_indicators.py
│   └── base_indicators.py
├── models
│   ├── hybrid_model.py
│   ├── ppo_trainer.py
│   └── rule_based.py
├── notebooks
│   └── explora_features.ipynb
├── README.md
├── requirements.txt
├── run_live.py
├── test.py
├── train.py
└── utils
    ├── config.py
    └── visualizer.py

```

## Instalação

### Requisitos
- Python 3.7+
- Pip

### Dependências

Para instalar as dependências, basta rodar:

```bash
pip install -r requirements.txt
```

As principais bibliotecas necessárias são:

- **Stable Baselines3**: Para treinamentos com DRL.
- **TA-Lib / TA**: Para calcular indicadores técnicos (RSI, MACD, SMA).
- **Matplotlib**: Para gerar gráficos de performance.
- **Pandas**: Para manipulação e análise de dados.
- **yfinance**: Para obter dados históricos de mercado.

## Como usar

### Passo 1: Treinar o modelo

Para treinar o modelo, basta rodar o script de treino:

```bash
python models/ppo_trainer.py
```

Este script irá treinar o modelo **Proximal Policy Optimization (PPO)** usando os dados históricos e indicadores técnicos.

### Passo 2: Testar o modelo

Após o treinamento, você pode testar o modelo com dados nunca vistos para ver como ele se comporta em situações reais:

```bash
python test.py
```

### Passo 3: Executar em tempo real (Paper Trading)

O bot pode ser executado em modo **paper trading** com qualquer corretora que ofereça acesso a dados e execução de ordens. No exemplo abaixo, estamos utilizando uma API simulada.

```bash
python run_live.py
```

Esse script irá tomar decisões de compra/venda com base no modelo treinado e acompanhar a evolução da carteira.

### Passo 4: Análise de Resultados (Backtest)

Para realizar a avaliação do modelo em dados históricos, basta rodar o seguinte comando:

```bash
python evaluation/backtest.py
```

Este script irá mostrar um gráfico da evolução da carteira e métricas como **lucro total**, **drawdown máximo** e **sharpe ratio**.

## Contribuição

Sinta-se à vontade para contribuir com o projeto, seja com melhorias no código, novas estratégias ou correções de bugs.

## Licença

Este projeto é licenciado sob a Licença MIT.

---