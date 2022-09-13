import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from IPython.display import display
import keras
from keras import Sequential
from keras.layers import Dense, LSTM, Dropout




def predict(main_df):
    df = main_df
    df = df[['DateTime', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
    data_training = df[df['DateTime'] < pd.to_datetime('2022-06-17')].copy()
    data_test = df[df['DateTime'] > pd.to_datetime('2022-06-16')].copy()
    training_data = data_training.drop(['DateTime', 'Adj Close'], axis = 1)
    scaler = MinMaxScaler()
    training_data = scaler.fit_transform(training_data)
    X_train = [] 
    Y_train = []
    training_data.shape[0]
    for i in range(60, training_data.shape[0]):
        X_train.append(training_data[i-60:i])
        Y_train.append(training_data[i,0])
    X_train, Y_train = np.array(X_train), np.array(Y_train)
    model = Sequential()
    model.add(LSTM(units = 50, activation = 'relu', return_sequences = True, input_shape = (X_train.shape[1], 5)))
    model.add(Dropout(0.2))
    model.add(LSTM(units = 60, activation = 'relu', return_sequences = True))
    model.add(Dropout(0.3))
    model.add(LSTM(units = 80, activation = 'relu', return_sequences = True))
    model.add(Dropout(0.4))
    model.add(LSTM(units = 120, activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(units =1))
    model.compile(optimizer = 'adam', loss = 'mean_squared_error')
    history= model.fit(X_train, Y_train, epochs = 20, batch_size =50, validation_split=0.1)
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(len(loss))
    plt.figure()
    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'r', label='Validation loss')
    plt.title("Training and Validation Loss")
    plt.legend()
    plt.show()
    part_60_days = data_training.tail(60)
    df= part_60_days.append(data_test, ignore_index = True)
    df = df.drop(['DateTime', 'Adj Close'], axis = 1)
    inputs = scaler.transform(df)
    X_test = []
    Y_test = []
    for i in range (60, inputs.shape[0]):
        X_test.append(inputs[i-60:i])
        Y_test.append(inputs[i, 0])
        X_test, Y_test = np.array(X_test), np.array(Y_test)
    Y_pred = model.predict(X_test)
    plt.figure(figsize=(14,5))
    plt.plot(Y_test, color = 'red', label = 'Real Bitcoin Price')
    plt.plot(Y_pred, color = 'green', label = 'Predicted Bitcoin Price')
    plt.title('Bitcoin Price Prediction using RNN-LSTM')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    list = data_test['DateTime']
    pred_df = pd.DataFrame()
    pred_df['Date'] = list
    pred_df['Predicted Price'] = Y_pred
    pred_df['Actual Price'] = Y_test
    display(pred_df)




    


