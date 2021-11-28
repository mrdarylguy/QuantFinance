import numpy as np
import scipy
import matplotlib.pyplot as plt
import yfinance as yf

class Options:
    def __init__(self):
        self.original_underlying = 100.0
        self.strike_prices = [120, 150, 180, 200, 220]
        self.option_prices = [5, 10, 15, 20, 30]
        self.quantities = [50, 40, 30, 20, 10]
        self.current_underlying = 190
        self.PnL = []
        self.cumm_PnL = []

        
        for strike, option, quantity in zip(self.strike_prices,
                                            self.option_prices,
                                            self.quantities):

                                            profit = quantity*(strike - option - self.original_underlying)
                                            self.PnL.append(profit)
                                            self.cumm_PnL.append(sum(self.PnL))

        for i, quantity in enumerate(self.quantities):
            x = self.strike_prices[i]
            y = self.cumm_PnL[i]
            z = str(quantity)+" calls"+" at $"+str(x)
            plt.plot(x, y, 'o')
            plt.text(x+2, y-5, z, fontsize=7)

        plt.axvline(x=self.current_underlying, ymin=0, ymax=10000, linewidth=1, color='r', 
                    label="Current price of underlying")
        plt.plot(self.strike_prices, self.cumm_PnL, "-", color="b", label="PnL")
        plt.ylabel('Profit ($)', fontsize=10)
        plt.xlabel('Strike price ($)', fontsize=10)
        plt.title('Long Call', fontsize=12)
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()

if __name__ == "__main__":
    Options()


        

        


        
