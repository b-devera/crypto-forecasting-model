# ReadMe
## Description
This script utilizes machine learning algorithms to predict the price movements of a particular cryptocurrency.
## General Workflow
1. Create dataframe with all desired information
2. Predict the directions of the price movement from 6/18/22 to 7/29/22 using K-Nearest Neighbors Classifier
3. Predict the price from 6/18/22 to 7/29/22 using Neural Network
4. Plot price predictions
5. Use KNN predictions to determine strength of prediction
6. Save the plot to machine

## Requirements
### System Requirements
* Python 3.x
### Python Libraries:
sklearn, numpy, keras, math, cProfile, pandas, IPython, matplotlib, datetime, requests, yfinance
## Usage
Change ticker to one of ten selected cryptocurrencies. Run ```technical_runner.py```.
## Detailed Workflow
### Create dataframe with all desired information
The dataframe is first aggregated using the ```data_preproc.py``` module. The dataframe is filled with values from the respective CSV file and the OHLC values from Yahoo Finance. Additionally, the BTC Dominance is appended from CoinMarketCap. However, not all of these features will be used for the K-Nearest Neighbors Classifier. As a result, a new dataframe is created with the following features: Date, Open, Bull/Bear Difference, and Profit/Loss Difference. Using the Open prices, a new column called Direction is calculated and appended to the dataframe.
### Predict the directions of the price movement from 6/18/22 to 7/29/22 using K-Nearest Neighbors Classifier
Using the dedicated dataframe created from the previous step, a KNN Classifier is used to predict directional price movements in the ```knn.py``` module. The Date column is dropped at the data is split into training and testing. The training data contains all data from 1/1/22 to 6/17/22. The testing data contains all data from 6/18/22 to 7/29/22. The KNN Classifier model is initialized with 30 neighbors and fitted using the training data. The fitted model is used to predict the directional movements.
### Predict the price from 6/18/22 to 7/29/22 using Neural Network
Before predicting the price values, a new dedicated dataframe for the Neural Network model is created in the ```data_preproc.py``` module. The feature used in this dataframe is the Open price. The training and testing data length is synonomous to the ones used for the KNN Classifier. The prediction is computed in the ```neural_network_open.py``` module. The data is first scaled using a Min-Max scaler in the range (0, 1). This univariate sequential model has the following ordered layers: LSTM (50 neurons), LSTM (50 neurons), Dense (25 units), and Dense (1 unit). These layers are compiled with the 'adam' optimizer and mean-squared-error for the loss. With a batch size of 16 and 200 epochs, the model is fitted using the training Open prices. The fitted model then makes predictions for future prices. The predicts are then unscaled and returned.
### Plot price predictions
The predictions made from the Neural Network model are then plotted on a graph in the ```technical_runner.py``` module. 
### Use KNN predictions to determine strength of prediction
Using the predicted directions from the KNN model, the strength of the Neural Network predictions are determined. For example, if the Neural Network model predicts that the price will increase, but the KNN model predicts the price will decrease, this prediction will be marked as weak. Alternatively, if both models predict the price will increase or decrease, the prediction is marked as strong.
### Save the plot to machine
Finally, the plot is saved as a PNG to the machine.


