from cProfile import label
import json
from typing import final
import pandas as pd
import neural_network_open
import data_preproc
from IPython.display import display
import data_analysis
import knn
from matplotlib import pyplot as plt
from datetime import date
import numpy as np


ticker = 'BTC-USD'

print("\n===============KNN PREDICTION==========================")
knn_df = data_preproc.create_knn_df(ticker)
preds, valids, dir_train = knn.predict(knn_df)

# print("\n===============NEURAL NETWORK PREDICTION===============")
nn_df = data_preproc.create_nn_df(ticker)
final_pred, final_val = neural_network_open.predict(nn_df)

# print("\n===================Data Visualization==================")
pd_dr = pd.date_range(date(2022, 6, 18), date(2022, 7, 29), freq='d')
date_list = []
for x in pd_dr:
    x = str(x)[0:10]
    date_list.append(x)
title = ticker + " Price Prediction"


# xi = list(range(len(date_list)))
# plt.plot(final_pred, label='Prediction')
# plt.plot(final_val, '--', color='y', label='Actual')
# plt.plot(date_list[0], final_pred[0], '^', markersize=5, color='b', label='Strong Upward Directional Prediction')
# plt.plot(date_list[0], final_pred[0], '^', markersize=5, color='r', label='Weak Upward Directional Prediction')
# plt.plot(date_list[0], final_pred[0], 'v', markersize=5, color='b', label='Strong Downward Directional Prediction')
# plt.plot(date_list[0], final_pred[0], 'v', markersize=5, color='r', label='Weak Downward Directional Prediction')
# plt.plot(date_list[0], final_pred[0], '^', markersize=5, color='w')
# plt.plot(date_list[0], final_pred[0], '^', markersize=5, color='w')
# plt.plot(date_list[0], final_pred[0], 'v', markersize=5, color='w')
# plt.plot(date_list[0], final_pred[0], 'v', markersize=5, color='w')
# for i in range(len(date_list)):
#     if i != len(date_list) - 1:
#         if preds[i] == 1:
#             x = i
#             y = final_pred[i]
#             if final_pred[i] < final_pred[i+1]:
#                 plt.plot(x, y, '^', markersize=5, color='b')
#             else:
#                 plt.plot(x, y, '^', markersize=5, color='r')
#         if preds[i] == 0:
#             x = i
#             y = final_pred[i]
#             if final_pred[i] > final_pred[i+1]:
#                 plt.plot(x, y, 'v', markersize=5, color='b')
#             else:
#                 plt.plot(x, y, 'v', markersize=5, color='r')
# plt.xticks(xi, date_list, rotation=45)
# plt.tick_params(axis='x', labelsize=5)
# plt.xlabel('Date', fontdict={'fontsize': 15})
# plt.ylabel('Price', fontdict={'fontsize': 15})
# plt.title(title, fontdict={'fontsize': 25})
# plt.legend(prop={'size': 8})
# plt.savefig(title)


final_pred = final_pred.tolist()
final_val = final_val.tolist()

exported_predictions = {
    'data': [

    ]
}

for i in range(len(date_list)):
    temp_dict = {
        'date': date_list[i],
        'prediction': round(final_pred[i][0], 2),
        'validation': round(final_val[i][0], 2)
    }
    exported_predictions['data'].append(temp_dict)


file_name = title + '.json'
with open(file_name, 'w') as json_file:
    json.dump(exported_predictions, json_file)
