from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier



def predict(main_df):
    df = main_df
    df.drop(labels='Date', axis=1, inplace=True)
    data = df.iloc[:,[0, 1, 2]]
    target = df.iloc[:,[3]]
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, shuffle=False)
    knn = KNeighborsClassifier(n_neighbors=30)
    knn.fit(x_train, y_train.values.ravel())
    predictions = knn.predict(x_test)
    validation = []
    for x in y_test.values.tolist():
        validation.append(x[0])
    return predictions.tolist(), validation, y_train['Direction'].tolist()
