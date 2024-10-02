
Stock_market_prediction
=======


## Prerequisites
- Python 3.x
- Django
- Other dependencies

### Clone the Repository
```bash



#Set Up Virtual Environment
python3 -m venv venv
source venv/bin/activate

###Install Dependencies
pip install -r requirements.txt



###Running the Development Server
python manage.py runserver


#Stock Price Prediction Using LSTM
This project implements a Long Short-Term Memory (LSTM) model
 to predict the next stock price value for two companies: Microsoft (MSFT) and Google (GOOGL).

#Features
LSTM Model: Utilizes a powerful neural network architecture to analyze and forecast stock prices based on historical data.
Live Data Integration: Fetches real-time stock price data from the Yahoo Finance API to ensure predictions are based on the latest information.
Stocks Covered: The project currently focuses on predicting stock prices for Microsoft (MSFT) and Google (GOOGL).

#How It Works
Data Collection: The model retrieves live stock price data using the Yahoo Finance API.
Data Preprocessing: Historical stock price data is preprocessed to be suitable for LSTM training.
Model Training: The LSTM model is trained on historical data to learn patterns and trends.
Prediction: The model predicts the next stock price value based on the trained data and the latest live data.




