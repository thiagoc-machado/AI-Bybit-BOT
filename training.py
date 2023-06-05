import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from trading_env import TradingEnv  # Este é o ambiente de negociação que você precisa criar
from config import Config
import pandas as pd
from keras.callbacks import ProgbarLogger
import matplotlib.pyplot as plt
from rl.callbacks import Callback
from models import create_model, create_and_print_model

class RewardLogger(Callback):
    def __init__(self):
        self.rewards = []

    def on_episode_end(self, episode, logs):
        self.rewards.append(logs['episode_reward'])

reward_logger = RewardLogger()

# Carrega os dados históricos
print('Carregando os dados histéricos')
data = pd.read_csv(f'historical_data_{Config.SYMBOL}.csv')
print(data.shape) 
data = data.drop('symbol', axis=1)
print(data.head())
# Cria o ambiente de negociação
print("Criando o ambiente de negociação")
env = TradingEnv(data)

# Define o modelo de aprendizado profundo
print( "Definindo o modelo de aprendizado profundo")
model = create_and_print_model(Config.IA_SETTINGS['window_length'], 11, env.action_space.n)



#model = Sequential()
# model.add(Flatten(input_shape=(10, 11)))
# model.add(Dense(16, activation='relu'))
# model.add(Dense(16, activation='relu'))
# model.add(Dense(16, activation='relu'))
# model.add(Dense(env.action_space.n, activation='linear'))

# Define a memória e a política
print("Definindo a memória e a política")
memory = SequentialMemory(limit=Config.IA_SETTINGS['SequentialMemoryLimit'], window_length=Config.IA_SETTINGS['window_length'])
policy = BoltzmannQPolicy()

# Cria o agente DQN
print("Criando o agente Deeper Q-Network")
dqn = DQNAgent(model=model, nb_actions=env.action_space.n, memory=memory, nb_steps_warmup=10,
               target_model_update=1e-2, policy=policy)
dqn.compile(Adam(learning_rate=Config.IA_SETTINGS['learning_rate']), metrics=['mae'])

# Treina o agente
print("Treinando o agente Deeper Q-Network")
callbacks = [ProgbarLogger()]
dqn.fit(env, nb_steps=50000, visualize=False, verbose=2, callbacks=[reward_logger])
history = dqn.fit(env, nb_steps=Config.IA_SETTINGS['steps'], visualize=False, verbose=2)


plt.plot(reward_logger.rewards)
# Plot the training history
#plt.plot(history.history['episode_reward'])
plt.title('Model training reward')
plt.ylabel('Reward')
plt.xlabel('Episode')
plt.show()

# Salva os pesos do modelo treinado
print("Salvando os pesos do modelo treinado")
dqn.save_weights(f'dqn_weights_{Config.SYMBOL}.h5f', overwrite=True)
