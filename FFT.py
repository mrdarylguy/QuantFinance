import numpy as np
import matplotlib.pyplot as plt

def obscured_signal():

    dt=0.001
    t=np.arange(0,1,dt)
    f=np.sin(2*np.pi*50*t)+np.sin(2*np.pi*120*t) #sum of 2 frequencies
    f_clean = f  
    f=f+2.5*np.random.randn(len(t))              #Add some noise

    plt.rcParams['figure.figsize'] = [10, 6]
    plt.rcParams.update({'font.size': 18})
    plt.plot(t,f,color='pink', linewidth=1.5, label='Noisy signal')
    plt.plot(t,f_clean,color='blue',linewidth=2, label='True signal')
    plt.xlim(t[0],t[-1])
    plt.xlabel('Radians')
    plt.ylabel('Amplitude')
    plt.title("True Signal obscured by noise")
    plt.legend()
    plt.show() 
    # fig = plt.figure()
    # return fig



