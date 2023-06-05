import gym
from gym import spaces
import numpy as np
from config import Config


class TradingEnv(gym.Env):
    def __init__(self, data):
        super(TradingEnv, self).__init__()

        # Definir o espaço de ação e observação
        self.action_space = spaces.Discrete(5)  # entra_long, sai_long, entra_short, sai_short, segura
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(data.shape[1],))

        # Inicializar o estado
        self.data = data
        self.current_step = 0

    def step(self, action):
        # Importar as configurações
        reward_multiplier = Config.IA_SETTINGS['reward_multiplier']
        penalty_multiplier = Config.IA_SETTINGS['penalty_multiplier']

        # Obter o preço atual e o próximo preço
        self.current_price = self.data.iloc[self.current_step]['close']
        self.next_price = self.data.iloc[self.current_step + 1]['close'] if self.current_step + 1 < len(self.data) else self.current_price

        # Aplicar a ação e obter a recompensa
        reward = 0
        if action == 'SELL' and self.position:
            reward = (self.next_price - self.current_price) * reward_multiplier
            self.position = None
        elif action == 'BUY':
            self.position = self.current_price
        elif action == 'HOLD' and self.position:
            reward = -0.1 * penalty_multiplier

        # Atualizar o estado
        self.current_step += 1
        done = self.current_step >= len(self.data)

        return self.data.iloc[self.current_step], reward, done, {}


    def reset(self):
        # Resetar o estado
        self.current_step = 0
        return self.data.iloc[self.current_step]


    def render(self, mode='human'):
        # Renderizar o ambiente
        pass

    def close(self):
        # Fechar o ambiente
        pass
