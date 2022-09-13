import data_processing
import knn_price
import neural_network_open
import data_preproc
from IPython.display import display
import knn_dir
import neural_network

#df = data_processing.create_dataframe('BTC-USD', '1y')
start_date = '2022-01-01'
end_date = '2022-07-29'
df = data_preproc.create_df()
# display(df)
# print(df.dtypes)

#KNN
print("\n===============KNN PREDICTION==========================")
#knn_price.predict(df, start_date, end_date)
knn_result, knn_accuracy = knn_dir.predict(df)
print(knn_accuracy)


#NN
print("\n===============NEURAL NETWORK PREDICTION===============")

# neural_network_open.predict(df)
neural_network.predict(df)