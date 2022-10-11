import neural_network_open
import data_preproc
from IPython.display import display
import data_analysis
import knn

ticker = 'BTC-USD'

print("\n===============KNN PREDICTION==========================")
knn_df = data_preproc.create_knn_df(ticker)
preds, valids, dir_train = knn.predict(knn_df)
# data_analysis.analyze(preds, valids, classification=True)

print("\n===============NEURAL NETWORK PREDICTION===============")
nn_df = data_preproc.create_nn_df(ticker, dir_train, preds)
neural_network_open.predict(nn_df)
