import numpy as np
import matplotlib.pyplot as plt

class FFT:
    def __init__(self):
        self.dt = 0.001
        self.time = np.arange(0, 1, self.dt)
        self.signal = np.sin(2*np.pi*50*self.time)+np.sin(2*np.pi*120*self.time)
        self.noise = 2.5*np.random.randn(len(self.time))  
        self.noisy_signal = self.signal + self.noise 

    def obscured_signal(self):
        
        plt.rcParams['figure.figsize'] = [10, 6]
        plt.rcParams.update({'font.size': 18})

        plt.plot(self.time, self.noisy_signal, color='pink', linewidth=1.5, label='Noisy signal')
        plt.plot(self.time, self.signal, color='blue',linewidth=2, label='True signal')
        plt.xlim(self.time[0],self.time[-1])
        plt.xlabel('Radians')
        plt.ylabel('Amplitude')
        plt.title("True Signal obscured within noise")
        plt.legend()
        plt.show()
        plot = plt.figure()
        return plot

    def freqeuncy_domain(self):
        n = len(self.time)
        fhat = np.fft.fft(self.noisy_signal, n)    #compute the FFT
        PSD = fhat * np.conj(fhat)/n               #power spectrum (power per frequency)
        freq = (1/(self.dt*n)) * np.arange(n)      #x-axis of frequencies 
        L = np.arange(1,np.floor(n/2),dtype='int') #only plot 1st half

        plt.plot(freq[L], PSD[L],color='red',LineWidth=2, label='Noisy')
        plt.xlim(freq[L[0]],freq[L[-1]])
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power Spectral Density')
        plt.legend()
        plt.show()

        plot = plt.figure()
        return plot




