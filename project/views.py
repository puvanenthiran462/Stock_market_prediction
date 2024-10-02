from django.shortcuts import render
from django.http import HttpResponse
# Create your models here.
from django.db import models
import requests
import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import joblib
import os
from sklearn.preprocessing import MinMaxScaler


# Create your views here.

def index(request):
    return render(request,"index.html")





def asd(request):
    msft = yf.Ticker("MSFT")
    data = yf.download("MSFT", period='1y')

    data_set = data
    # Add RSI, EMA features
    data['RSI'] = ta.rsi(data['Close'], timeperiod=14)
    data['EMAF'] = ta.ema(data['Close'], timeperiod=12)
    data['EMAM'] = ta.ema(data['Close'], timeperiod=26)
    data['EMAS'] = ta.ema(data['Close'], timeperiod=50)

    # Calculate 'TargetNextClose' based on 'Close' price shifting one day ahead
    data['TargetNextClose'] = data['Close'].shift(-1)  # Predicting next day's close
    data_set['TargetNextClose'] = data_set['Close'].shift(-1)

   
    data.dropna(inplace=True)
    

#     data.reset_index(inplace=True)
    data.reset_index(inplace=True)
    
    # data_set.reset_index(inplace=True)

    # Extract the relevant features
    feature_columns = ['Open', 'High', 'Low', 'Adj Close', 'RSI', 'EMAF', 'EMAM', 'EMAS']
    data_input = data[feature_columns].tail(50)

    # Reshape the data for the model
    data_input = np.array(data_input).reshape(1, 50, 8)

    # Load the trained model and make predictions for the next 1 day (tomorrow)
    cls = joblib.load('ml_model/my_model.joblib')

    # Predict the next day's price based on the last 30 days of data
    predictions = cls.predict(data_input)
    predictions = predictions[0]   # Assuming your model gives normalized values
    data_mi = 40.290000915527344
    data_ma = 467.55999755859375
    predictions=predictions-0.9
    # Calculate the original predicted value manually
    predictions  = (predictions  * (data_ma - data_mi)) + data_mi

    last_50_days = data_set.tail(50)

    # Prepare the data for the graph
    labels = last_50_days['Date'].dt.strftime('%Y-%m-%d').tolist()  # Convert dates to strings
    target_next_close = last_50_days['TargetNextClose'].tolist()

    # Add the predicted next day to the graph data
    last_date = data_set['Date'].iloc[-1]
    next_day_1 = last_date + pd.Timedelta(days=1)
    
    labels.append(next_day_1.strftime('%Y-%m-%d'))
    target_next_close.append(predictions[0])  # Prediction for the next day's close

    return render(request, 'asd.html', {
        'labels': labels,               # Labels including last 50 days and next day
        'target_next_close': target_next_close,  # TargetNextClose for the last 50 days + prediction
        'next_day_1': next_day_1.strftime('%Y-%m-%d'),  # Date of the predicted next day
        'predictions': predictions,      # List of predictions for the next day
        'stock_name':'MICROSOFT  STOCK'
    })


def Google_price(request):
    msft = yf.Ticker("GOOGL")
    data = yf.download("GOOGL", period='1y')

    data_set = data
    # Add RSI, EMA features
    data['RSI'] = ta.rsi(data['Close'], timeperiod=14)
    data['EMAF'] = ta.ema(data['Close'], timeperiod=12)
    data['EMAM'] = ta.ema(data['Close'], timeperiod=26)
    data['EMAS'] = ta.ema(data['Close'], timeperiod=50)

    # Calculate 'TargetNextClose' based on 'Close' price shifting one day ahead
    data['TargetNextClose'] = data['Close'].shift(-1)  # Predicting next day's close
    data_set['TargetNextClose'] = data_set['Close'].shift(-1)

   
    data.dropna(inplace=True)
    

#     data.reset_index(inplace=True)
    data.reset_index(inplace=True)
    
    # data_set.reset_index(inplace=True)

    # Extract the relevant features
    feature_columns = ['Open', 'High', 'Low', 'Adj Close', 'RSI', 'EMAF', 'EMAM', 'EMAS']
    data_input = data[feature_columns].tail(30)

    # Reshape the data for the model
    data_input = np.array(data_input).reshape(1, 30, 8)

    # Load the trained model and make predictions for the next 1 day (tomorrow)
    cls = joblib.load('ml_model/Google_model.joblib')

    # Predict the next day's price based on the last 30 days of data
    predictions = cls.predict(data_input)
    predictions = predictions[0]   # Assuming your model gives normalized values
    data_min = 24.85300064086914
    data_max =  191.17999267578125
    predictions=predictions-4.17
    # Calculate the original predicted value manually
    predictions  = (predictions  * (data_max - data_min)) + data_min

    last_50_days = data_set.tail(50)

    # Prepare the data for the graph
    labels = last_50_days['Date'].dt.strftime('%Y-%m-%d').tolist()  # Convert dates to strings
    target_next_close = last_50_days['TargetNextClose'].tolist()

    # Add the predicted next day to the graph data
    last_date = data_set['Date'].iloc[-1]
    next_day_1 = last_date + pd.Timedelta(days=1)
    
    labels.append(next_day_1.strftime('%Y-%m-%d'))
    target_next_close.append(predictions[0])  # Prediction for the next day's close

    return render(request, 'Google_price.html', {
        'labels': labels,               # Labels including last 50 days and next day
        'target_next_close': target_next_close,  # TargetNextClose for the last 50 days + prediction
        'next_day_1': next_day_1.strftime('%Y-%m-%d'),  # Date of the predicted next day
        'predictions': predictions ,      # List of predictions for the next day
        'stock_name':'GOOGLE STOCK'
    })

def select(request):
    return render(request,"select.html")

