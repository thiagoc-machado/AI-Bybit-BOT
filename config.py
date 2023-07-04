# arquivo config.py

class Config:
    # API keys
    BYBIT_API_KEY = ""
    BYBIT_API_SECRET = ""

    # Parâmetros de trading
    INITIAL_INVESTMENT = 1000 # valor inicial de investimento
    SYMBOL = "BTCUSDT"
    INTERVAL = "15"  # tempo de velas
    HISTORICAL_DATA_PERIOD = "1Y"  # período dos dados para backtesting
    ORDER_TYPE = "Limit"  # tipo de ordem
    MARKET = "Futures"  # mercado de operação
    FROM_TIME = "2021-01-01"  # tempo de início do backtesting
    TO_TIME = "2023-05-31"  # tempo de término do backtesting

    # Configuração dos indicadores
    INDICATOR_SETTINGS = {
        "indicator1": {}#"param1": value1, "param2": value2},
        # adicione mais indicadores conforme necessário
    }

    # Parâmetros de ordem
    TAKE_PROFIT = 0.01  # 1%
    STOP_LOSS = 0.02  # 2%
    TRAILING_STOP_LOSS = 0.01  # 1%
    LEVERAGE = 10  # 10x
    USE_DCA = True  # se vai usar DCA
    DCA_VALUE = 0.01  # valor de DCA
    SLIPPAGE = 0.001  # 0.1%
    ENTRY_FEE = 0.00075  # taxa da corretora de entrada
    EXIT_FEE = 0.00075  # taxa da corretora de saída

    # Configuração da conta
    INITIAL_BALANCE = 1.0  # saldo inicial em BTC

    # Configuração da IA
    IA_SETTINGS = {
        "reward_multiplier": 1.0,
        "penalty_multiplier": 1.0,
        "learning_rate": 0.001,
        "SequentialMemoryLimit": 1500,  #00 limite de memória sequencial - Uma memória maior pode melhorar a performance do agente permitindo que ele aprenda de uma gama mais ampla de experiências passadas. No entanto, uma memória muito grande pode tornar o treinamento mais lento e consumir mais memória do seu computador.
        "window_length": 2,  #0 largura da janela - Um window_length maior pode permitir que o agente perceba tendências ao longo do tempo, mas também pode tornar o espaço de estados significativamente maior, tornando o problema mais difícil de resolver
        "steps": 5000,  #0 numero de steps do treinamento
    }

