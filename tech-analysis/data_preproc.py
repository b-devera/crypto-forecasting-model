from datetime import date
import pandas as pd
import yfinance as yf
from IPython.display import display
import requests
import numpy as np


def create_df(ticker):
    if ticker == 'BTC-USD':
        df1 = pd.read_csv('additional_data_btc.csv')
        df2 = pd.DataFrame(yf.download(tickers='BTC-USD', start='2022-01-01', end='2022-08-23'))
    df1 = df1.iloc[0:235]
    df1.reset_index(drop=True, inplace=True)
    df2.reset_index(drop=True, inplace=True)
    df = pd.concat([df1, df2], axis=1)
    df = df.iloc[0:210]
    response = requests.get(url='https://api.coinmarketcap.com/data-api/v3/global-metrics/quotes/historical?format=chart&interval=1d&timeEnd=1659164400&timeStart=2022-01-01')
    response = response.json()
    btc_dom = []
    for x in response['data']['quotes']:
        btc_dom.append(x['btcDominance'])
    df['BTC Dominance'] = btc_dom
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.precision', 3)
    date_list = pd.date_range(start='1/1/2022', end='7/29/2022')
    df['DateTime'] = date_list
    return df


def create_knn_df(ticker):
    raw_df = create_df(ticker=ticker)
    knn_df = pd.DataFrame()
    knn_df['Date'] = raw_df['DateTime']
    knn_df['Open'] = raw_df['Open']
    knn_df['Bull/Bear Difference'] = raw_df['Difference']
    knn_df['Profit/Loss Difference'] = raw_df['Profit'] - raw_df['Losses']
    knn_df['Direction'] = np.nan
    knn_df.at[0, 'Direction'] = 0
    num_columns = knn_df.shape
    num_columns = num_columns[1]
    num_columns = num_columns - 1
    for index, row in knn_df.iterrows():
        if index == 0:
            continue
        else:
            prev_close = knn_df.iloc[index-1,1]
            current_close = knn_df.iloc[index,1]
            if prev_close < current_close:
                knn_df.at[index, 'Direction'] = 1
            if prev_close > current_close:
                knn_df.at[index, 'Direction'] = 0
    knn_df['Direction'] = knn_df['Direction'].astype('category')
    return knn_df


def create_nn_df(ticker):
    df = create_df(ticker)
    nn_df = pd.DataFrame()
    nn_df['Open'] = df['Open']
    return nn_df




    

    
