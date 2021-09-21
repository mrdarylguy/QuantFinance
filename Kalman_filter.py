from pykalman import KalmanFilter
import numpy as np
import pandas as pd
from scipy import poly1d
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf

class Kalman:
    def __init__(self):
        self.ticker = yf.Ticker('TSLA')
        self.data = None

    def see_stock(self):
        data = self.ticker.history(period='max')
        data['Close'].plot(title='TSLA stock price ($)')
        plot = plt.figure()
        return plot

    def period_of_interest(self):
        self.data = yf.download('TSLA', 
                            start='2014-01-01',
                            end='2019-12-31',
                            progress=False)

        
        plt.figure(figsize=(15,5))
        self.data['Close'].plot(grid=True)
        plt.ylabel('Price ($)')
        plt.title('Tesla Price ($)')
        plot = plt.figure()
        return plot

    def kalman_filtered(self):
        kf = KalmanFilter(transition_matrices=[1],
                          observation_matrices=[1],
                          initial_state_mean=0,
                          initial_state_covariance=1,
                          observation_covariance=1,
                          transition_covariance=0.0001,)
      
        mean, cov = kf.filter(self.data['Close'].values)
        mean, std = mean.squeeze(), np.std(cov.squeeze())

if __name__ == "__main__":

    kalman = Kalman()
    # kalman.see_stock()
    kalman.period_of_interest()

    pass
    
    
    

