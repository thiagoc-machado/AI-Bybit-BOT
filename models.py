from keras.models import Sequential
from keras.layers import Dense, Flatten, Layer
import tensorflow as tf

class PrintShapeLayer(Layer):
    def call(self, inputs):
        print(inputs.shape)
        return inputs

def create_model(window_length, feature_size, action_size):
    model = Sequential()
    model.add(PrintShapeLayer(input_shape=(window_length, feature_size)))
    model.add(Flatten())
    model.add(Dense(24, activation='relu'))
    model.add(Dense(48, activation='relu'))
    model.add(Dense(action_size, activation='linear'))
    return model

def create_and_print_model(window_length, feature_size, action_size):
    model = Sequential()
    model.add(PrintShapeLayer(input_shape=(window_length, feature_size)))
    model.add(Flatten())
    model.add(Dense(24, activation='relu'))
    model.add(Dense(48, activation='relu'))
    model.add(Dense(action_size, activation='linear'))

    # Agora recrie o modelo sem a camada personalizada
    model = Sequential()
    model.add(Flatten(input_shape=(window_length, feature_size)))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(48, activation='relu'))
    model.add(Dense(action_size, activation='linear'))
    return model

