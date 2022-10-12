import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
import math


def predict(df):
    train_df = df.filter(['Open'])
    data_unscaled = train_df.values
    mmscaler = MinMaxScaler(feature_range=(0, 1))
    np_data = mmscaler.fit_transform(data_unscaled)
    sequence_length = 50
    index_Open = train_df.columns.get_loc("Open")
    train_data_len = math.ceil(np_data.shape[0] * 0.8)
    train_data = np_data[0:train_data_len, :]
    test_data = np_data[train_data_len - sequence_length:, :]
    def partition_dataset(sequence_length, train_df):
        x, y = [], []
        data_len = train_df.shape[0]
        for i in range(sequence_length, data_len):
            x.append(train_df[i-sequence_length:i,:])
            y.append(train_df[i, index_Open])
        x = np.array(x)
        y = np.array(y)
        return x, y
    x_train, y_train = partition_dataset(sequence_length, train_data)
    x_test, y_test = partition_dataset(sequence_length, test_data)
    model = Sequential()
    neurons = sequence_length
    model.add(LSTM(neurons, return_sequences=True, input_shape=(x_train.shape[1], 1))) 
    model.add(LSTM(neurons, return_sequences=False))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, batch_size=16, epochs=200)
    y_pred_scaled = model.predict(x_test)
    y_pred = mmscaler.inverse_transform(y_pred_scaled)
    y_test_unscaled = mmscaler.inverse_transform(y_test.reshape(-1, 1))
    return y_pred, y_test_unscaled


