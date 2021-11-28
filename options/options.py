import numpy as np
import scipy
import matplotlib.pyplot as plt
import yfinance as yf

class Options():
    def __init__(self,
                 orginal_underlying,
                 strike_prices,
                 option_prices,
                 quantities,
                 current_underlying,
                 PnL,
                 cumm_PnL,
                 costs):

        self.original_underlying = orginal_underlying
        self.strike_prices = strike_prices
        self.option_prices = option_prices
        self.quantities = quantities
        self.current_underlying = current_underlying
        self.PnL = PnL
        self.cumm_PnL = cumm_PnL
        self.costs = costs
        
        for strike, option, quantity in zip(self.strike_prices,
                                            self.option_prices,
                                            self.quantities):

                                            profit = quantity*(strike - option - self.original_underlying)
                                            self.PnL.append(profit)
                                            self.cumm_PnL.append(sum(self.PnL))

                                            self.costs -= option*quantity

        for i, quantity in enumerate(self.quantities):
            x = self.strike_prices[i]
            y = self.cumm_PnL[i]
            z = str(quantity)+" calls"+" at $"+str(x)
            plt.plot(x, y, 'o')
            plt.text(x+2, y-100, z, fontsize=8)

        plt.axvline(x=self.current_underlying, ymin=0, ymax=10000, linewidth=1, color='g', 
                    label="Current price of underlying: $%s"%self.current_underlying)

        plt.axhline(y=self.costs, xmin= -100, xmax=120, 
                    linewidth=1, color='r',
                    label="Cost to purchase calls: $%s"%-(self.costs))

        plt.plot(self.strike_prices, self.cumm_PnL, "-", color="b", label="PnL",)
        plt.ylabel('Profit ($)', fontsize=10)
        plt.xlabel('Strike price ($)', fontsize=10)
        plt.title('Long Calls from $%s - $%s, Bought at underlying=$%s'%(self.strike_prices[0], 
                                                                             self.strike_prices[-1],
                                                                             self.original_underlying), 
                   fontsize=10)

        plt.legend(loc="upper left", fontsize=9)
        plt.grid()
        plt.savefig("./options/options_plots/plot.png")
        plt.show()

if __name__ == "__main__":
    _option = Options(100,
                      [120, 150, 180, 200, 220],
                      [5, 10, 15, 20, 30],
                      [50, 40, 30, 20, 10],
                      190,
                      [],
                      [],
                      0)



        

        


        
