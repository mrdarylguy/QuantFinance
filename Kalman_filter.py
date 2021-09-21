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
        plt.plot(data['Close'])
        plt.title("TSLA price history ($)")
        plt.figure()
        plt.show()

    def period_of_interest(self):
        self.data = yf.download('TSLA', 
                            start='2014-01-01',
                            end='2019-12-31',
                            progress=False)

        self.data['Close'].plot(grid=True)
        plt.ylabel('Price ($)')
        plt.title('Period of interest: TSLA', fontsize=8)
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

        plt.plot(self.data['Close'].values - mean, 'red', lw=1.5)
        plt.title("Kalman filtered price fluctuation", fontsize=8)
        plt.ylabel("Deviation from the mean ($)")
        plt.xlabel("Days")
        plt.grid()
        plot = plt.figure(figsize=(12,6))
        return plot

    def combine_plots(self):
        figs, axs = plt.subplots(2,1)
        plt.tight_layout(pad=4.0)

        plt.sca(axs[0])
        plot0 = self.period_of_interest()

        plt.sca(axs[1])
        plot1 = self.kalman_filtered()

        plt.show()



if __name__ == "__main__":

    kalman = Kalman()
    
    kalman.see_stock()
    kalman.period_of_interest()
    kalman.kalman_filtered()
    kalman.combine_plots()

    pass
    
    
    

