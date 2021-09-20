import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import yfinance as yf

class FFT:
    def __init__(self):
        self.dt = 0.001
        self.time = np.arange(0, 1, self.dt)
        self.signal = np.sin(2*np.pi*50*self.time)+np.sin(2*np.pi*120*self.time)
        self.noise = 2.5*np.random.randn(len(self.time))  
        self.noisy_signal = self.signal + self.noise

        self.PSD = None
        self.fhat = None 

    def obscured_signal(self):
        
        plt.rcParams['figure.figsize'] = [10, 6]
        plt.rcParams.update({'font.size': 18})

        plt.plot(self.time, self.noisy_signal, color='pink', linewidth=1.5, label='Noisy signal')
        plt.plot(self.time, self.signal, color='blue',linewidth=2, label='True signal')
        plt.xlim(self.time[0],self.time[-1])
        plt.xlabel('Radians')
        plt.ylabel('Amplitude')
        plt.title("True Signal obscured within noise", fontsize=12)
        plt.legend(prop={"size":8}, loc='upper right')
        plot = plt.figure()
        return plot

    def freqeuncy_domain(self):
        n = len(self.time)
        self.fhat = np.fft.fft(self.noisy_signal, n)    #compute the FFT
        self.PSD = self.fhat * np.conj(self.fhat)/n     #power spectrum (power per frequency)
        freq = (1/(self.dt*n)) * np.arange(n)      #x-axis of frequencies 
        L = np.arange(1,np.floor(n/2),dtype='int') #only plot 1st half

        plt.plot(freq[L], self.PSD[L],color='red',linewidth=2, label='Noisy')
        plt.xlim(freq[L[0]],freq[L[-1]])
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power Spectral Density', fontsize=10)
        plt.legend(prop={"size":10}, loc='upper right')
        plot = plt.figure()
        return plot

    def filter_signal(self):
        indices = self.PSD > 100
        PSDclean = self.PSD * indices
        self.fhat = indices * self.fhat
        inv_fft = scipy.fft.ifft(self.fhat)

        plt.plot(self.time, inv_fft, color='blue', linewidth=1.5, label='filtered')
        plt.xlim(self.time[0], self.time[-1])
        plt.xlabel("Radians")
        plt.ylabel('Amplitude')
        plt.legend(prop={"size":10}, loc='upper right')
        plot = plt.figure()
        return plot

    def combine_plots(self):

        fig, axs = plt.subplots(3, 1)

        plt.sca(axs[0])
        plot1 = self.obscured_signal()

        plt.sca(axs[1])
        plot2 = self.freqeuncy_domain()

        plt.sca(axs[2])
        plot3 = self.filter_signal()

        plt.tight_layout()
        plt.show()

class FFT_stock:
    def __init__(self):
        self.ticker = yf.Ticker("TSLA")
        self.price_dataframe = None

    def price_chart(self):
        tsla_df = self.ticker.history(period='max')
        tsla_df['Close'].plot(title='TSLA Price ($)')
        plt.show()

    def period_of_interest(self):
        df = yf.download('TSLA', start="2021-01-01", end="2021-09-01", progress=False)
        df = df[:1000]
        df = df[['Close']]
        plt.show()
        
        df.plot(grid=True)
        plt.ylabel("Price ($)")
        plt.title("TSLA Price ($)")
        plot = plt.figure(figsize=(10,3))
        plt.show()

        self.price_dataframe = df

    def frequency_domain(self):

        df = self.price_dataframe
        df['delta'] = np.append(np.array([0]), np.diff(df['Close'].values)) #Create dataframe for "delta"

        sp = scipy.fft.fft(df['delta'].values)
        df['Theta'] = np.arctan(sp.imag/sp.real)
        numValues = len(df)
        numValuesHalf = numValues/2
        df['Amplitude'] = np.sqrt(sp.real**2 + sp.imag**2) / numValuesHalf
        df['Freq'] = scipy.fft.fftfreq(sp.size, d=1)

       
        plt.plot(df['Freq'], df["Amplitude"].values, '.')
        plt.axvline(x=0, ymin=0, ymax=1, linewidth=1, color='r')

        plt.ylabel('Amplitude[$]', fontsize=8)
        plt.xlabel('Frequency[days]', fontsize=8)
        plt.title('Frequency domain', fontsize=12)
        plt.grid()
        plot = plt.figure(figsize=(10, 3))
        return plot

    def filtered_signal(self):
        df = self.price_dataframe
        
        meanAmp = df["Amplitude"].mean()
        stdAmp = df["Amplitude"].std()

        dominantAmpCheck = df["Amplitude"] > (2*stdAmp + meanAmp) #3 std deviation above mean
        positiveFreqCheck = df['Freq'] > 0

        dominantAmp = df[dominantAmpCheck & positiveFreqCheck]['Amplitude']
        dominantFreq = df[dominantAmpCheck & positiveFreqCheck]['Freq']
        dominantTheta = df[dominantAmpCheck & positiveFreqCheck]['Theta']

        plt.plot(dominantFreq, dominantAmp, '.')
        plt.ylabel('Amplitude [$]', fontsize=8)
        plt.xlabel('Frequency [days]', fontsize=8)
        plt.title('Frequency Domain \n(Dominant & Positive)', fontsize=10)
        plt.grid()
        plot = plt.figure(figsize=(10,3))
        return plot

    def combine_fourier_plots(self):
    
        fig, axs = plt.subplots(2, 1)
        plt.tight_layout(pad=4.0)

        plt.sca(axs[0])
        plot2 = self.frequency_domain()

        plt.sca(axs[1])
        plot3 = self.filtered_signal()

        plt.show()


if __name__ == "__main__":
#     # fft = FFT()
#     # fft.combine_plots()
      fft_stock = FFT_stock()
      fft_stock.period_of_interest()
      fft_stock.combine_fourier_plots()



