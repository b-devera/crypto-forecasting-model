from sklearn import neighbors
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
import pandas as pd
import numpy as np
from  sklearn.metrics import accuracy_score
from IPython.display import display


def predict(main_df):
    df = main_df
    list = pd.to_numeric(df['DateTime'])
    df['DateTime'] = list
    df['Direction'] = np.nan
    for (columnName, columnData) in df.iteritems():
        df[columnName] = (df[columnName] - df[columnName].mean()) / df[columnName].std()
    df.at[0, 'Direction'] = 0
    for index, row in df.iterrows():
        if index == 0:
            continue
        else:
            prev_close = df.iloc[index-1,16]
            current_close = df.iloc[index,16]
            if prev_close < current_close:
                df.at[index, 'Direction'] = 1
            if prev_close > current_close:
                df.at[index, 'Direction'] = 0
    train_size = int(len(df.index)*0.8)
    train_data = df.iloc[:train_size]
    test_data = df.iloc[train_size-1:]
    train_x = train_data.drop(columns=['Direction'],axis=1)
    train_y = train_data['Direction']
    test_x = test_data.drop(columns=['Direction'],axis=1)
    test_y = test_data['Direction']
    knn = KNeighborsClassifier(n_neighbors=15)
    knn.fit(train_x, train_y)
    r = knn.predict(train_x)
    e = knn.predict(test_x)
    accuracy_train = accuracy_score(train_y, r)
    accuracy_test = accuracy_score(test_y, e)
    pred_df = pd.DataFrame()
    list = pd.to_datetime(list)
    list = list[167:]
    pred_df['Date'] = list
    pred_df['Predicted Direction'] = e
    pred_df['Actual Direction'] = test_y
    list = pd.to_datetime(test_data['DateTime'])
    return pred_df, accuracy_test


