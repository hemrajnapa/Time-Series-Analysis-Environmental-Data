import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

def plot_series(df, column):
    """Plot a time series from the dataframe"""
    df.set_index('Date', inplace=True)
    df[column].plot(figsize=(10,6))
    plt.title(f'Time Series of {column}')
    plt.show()

def check_stationarity(series):
    """Check the stationarity of a time series using the Augmented Dickey-Fuller test"""
    result = adfuller(series.dropna())
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    return result[1] < 0.05  # If p-value < 0.05, the series is stationary

def fit_arima_model(series, order=(1,1,1)):
    """Fit ARIMA model to the time series"""
    model = ARIMA(series, order=order)
    model_fit = model.fit()
    print(model_fit.summary())
    return model_fit

def forecast(model_fit, steps=10):
    """Make future predictions using ARIMA model"""
    forecast = model_fit.forecast(steps=steps)
    return forecast

if __name__ == "__main__":
    filepath = 'path_to_your_data.csv'
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Plotting and checking stationarity
    plot_series(df, 'Rainfall_Bastia_Umbra')
    stationary = check_stationarity(df['Rainfall_Bastia_Umbra'])
    
    # Fitting ARIMA if series is stationary
    if stationary:
        model_fit = fit_arima_model(df['Rainfall_Bastia_Umbra'])
        print(forecast(model_fit, steps=10))
    else:
        print("Series is not stationary.")
