import requests
import pandas as pd
from config import Config
from datetime import datetime, timedelta
import time

# Transformar o tempo de início e término em timestamp
start_time = int(datetime.strptime(Config.FROM_TIME, "%Y-%m-%d").timestamp())
end_time = int(datetime.strptime(Config.TO_TIME, "%Y-%m-%d").timestamp())

# URL da API para buscar os dados históricos
url = "https://api.bybit.com/public/linear/kline?symbol={}&interval={}&from={}&limit=200"

# Inicializar um dataframe vazio para armazenar os dados
df = pd.DataFrame()

i=0
# Fazer várias requisições para obter todos os dados
while start_time < end_time:
    response = requests.get(url.format(Config.SYMBOL, Config.INTERVAL, start_time))
    data = response.json()
    
    # Adicionar os dados ao dataframe
    if data['result'] is not None:
        # Adicionar os dados ao dataframe
        df = pd.concat([df, pd.DataFrame(data['result'])])

        # Atualizar o tempo de início para a próxima requisição
        start_time = data['result'][-1]['open_time'] + 1
    else:
        print("No data returned from the API.")
    
    # Pausar por um segundo para evitar sobrecarregar a API
    i += 1
    print(f'Baixando dados: round {i} restando: {int((end_time-start_time)/86400)} dias', end='\r')
    time.sleep(1)

# Salvar os dados em um arquivo CSV
print('\nDownload efetuado com sucesso')
df.to_csv(f'historical_data_{Config.SYMBOL}.csv', index=False)
print('Arquivo CSV salvo com sucesso')
