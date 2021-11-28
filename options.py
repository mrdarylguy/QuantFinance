import numpy as np
import scipy
import matplotlib.pyplot as plt
import yfinance as yf

class Options:
    def __init__(self):
        self.current_underlying = 100.0
        self.strike_prices = [120, 150, 180, 200, 220]
        self.option_prices = [5, 10, 15, 20, 30]
        self.quantities = [50, 40, 30, 20, 10]
        self.PnL = []
        self.cumm_PnL = []

        
        for strike, option, quantity in zip(self.strike_prices,
                                            self.option_prices,
                                            self.quantities):

                                            profit = quantity*(strike - option - self.current_underlying)
                                            self.PnL.append(profit)
                                            self.cumm_PnL.append(sum(self.PnL))

        
        plt.plot(self.strike_prices, self.cumm_PnL, '-o')
        plt.ylabel('Profit ($)', fontsize=10)
        plt.xlabel('Strike price ($)', fontsize=10)
        plt.title('Long Call', fontsize=12)
        plt.grid()
        plt.show()

if __name__ == "__main__":
    Options()


        

        


        
