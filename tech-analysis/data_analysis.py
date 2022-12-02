import pandas as pd
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import numpy as np

from knn_dir import predict

def analyze(pred, val, classification=False):
    # Runner
    print('Error Metrics==========')
    print('Classification Metrics======')
    error_metrics(pred=pred, val=val)
    if classification:
        classification_metrics(pred=pred, val=val)
    


def error_metrics(pred, val):
    mse = mean_squared_error(val, pred)
    print("Mean Squared Error: " + str(mse))
    rmse = np.sqrt(mse)
    print("Root Mean Absolute Error: " + str(rmse))


def classification_metrics(pred, val):
    acc_score = accuracy_score(val, pred)
    print("Accuracy Score: " + str(acc_score))
    con_matrix = confusion_matrix(val, pred)
    print("Confusion Matrix: \n", con_matrix)
    tn, fp, fn, tp = con_matrix.ravel()
    print("Predicted '0' Correctly: " + str(tn))
    print("Predicted '1' Correctly: " + str(tp))
    print("Predicted '1' Incorrectly: " + str(fp))
    print("Predicted '0' Incorrectly: " + str(fn))
    prec = precision_score(val, pred, zero_division=1)
    rec = recall_score(val, pred)
    f = f1_score(val, pred)
    print("Precision (Percent Chance '1' is Predicted): " + str(prec))
    print("Recall: " + str(rec))
    print("F1 Score: " + str(f))

