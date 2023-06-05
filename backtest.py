from rl.policy import GreedyQPolicy
from rl.agents.dqn import DQNAgent
from keras.optimizers import Adam
import pandas as pd
from trading_env import TradingEnv
from config import Config
from rl.memory import SequentialMemory
from models import create_model, create_and_print_model

def main():
    # Create the environment
    data = pd.read_csv(f'historical_data_{Config.SYMBOL}.csv')
    print(data.shape)
    env = TradingEnv(data)
    print(f"Observation space shape: {env.observation_space.shape}")

    # Get the state_size and action_size from the environment
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n

    # Create the model with the correct state_size and action_size
    model = create_and_print_model(Config.IA_SETTINGS['window_length'], 12, env.action_space.n)


    # Create the agent
    memory = SequentialMemory(limit=Config.IA_SETTINGS['SequentialMemoryLimit'], window_length=Config.IA_SETTINGS['window_length'])
    policy = GreedyQPolicy()
    dqn = DQNAgent(model=model, nb_actions=env.action_space.n, memory=memory, policy=policy, test_policy=policy)
    dqn.compile(Adam(learning_rate=Config.IA_SETTINGS['learning_rate']), metrics=['mae'])

    # Load the weights from disk
    dqn.load_weights(f'dqn_weights_{Config.SYMBOL}.h5f')

    # Run the backtest
    obs = env.reset()
    done = False
    while not done:
        action = dqn.forward(obs)
        obs, reward, done, info = env.step(action)
        print(f"Step: {env.current_step}, Action: {action}, Reward: {reward}, Balance: {env.balance}, Positions: {env.positions}")

if __name__ == "__main__":
    main()
