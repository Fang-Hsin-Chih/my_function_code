import datetime
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pywt
import scaleogram as scg
import seaborn as sns
from dateutil.relativedelta import relativedelta

#Whole Year
def Wavelet_Spectrum_WS(data,sampling_time,year,wavelet='cmor0.7-1.5'):
    dt = 1/sampling_time
    time   =  np.arange(len(data))*dt
    data.fillna(method='ffill',inplace=True)
    signal = data['WS95'].copy() - data['WS95'].mean()
    scales = np.logspace(0, 5, num=350, dtype=np.int32)
    fig, (ax) = plt.subplots(1, 1,figsize=(18,8))
    scg.cws(time,signal, scales,clim=(0,50),
            cbar= 'horizontal',cmap='inferno',cbarlabel='Amplitude (absCWT)',
            cbarkw={'aspect':45, 'pad':0.15,'shrink':0.5, 
                    'fraction':0.05,'ticks':[0,10,20,30,40,50]},
            ylabel="Period [hour]", xlabel='minute',yscale='log',ax=ax)
    y_tic = [1,2,4,8,12,16,24,32,64,128]
    ax.set_yticks(y_tic)
    ax.set_yticklabels(y_tic)
    m_day = [0,31,28,31,30,31,30,31,31,30,31,30]
    x_tic = np.array(m_day)*24
    x_tic2 = x_tic.copy()
    for i in range(len(x_tic)):
        x_tic2[i] = int(x_tic[i] + x_tic[:i].sum())
    base = data['DateTime'].iloc[0]
    mon = ['01','02','03','04','05','06','07','08','09','10','11','12']
    arr=np.array(["{}-{}".format(base.year,mon[i]) for i in range(len(mon))])
    ax.set_xticks(x_tic2)
    ax.set_xticklabels(arr)
    ax.set_ylim(1,y_tic[-1])
    ax.tick_params(axis="x", labelsize=18)
    ax.tick_params(axis="y", labelsize=18)
    ax.set_ylabel("Period [hour]",size=20)
    ax.set_xlabel("Time [month]",size=18)
    ax.set_title("Contunuous Wavelet Transform of Wind Speed ({})".format(year),size=20)
    plt.show()

def Wavelet_Spectrum_WD(data,sampling_time,year,wavelet='cmor0.7-1.5'):
    dt = 1/sampling_time
    time   =  np.arange(len(data))*dt
    WD = data['WD95'].copy()
    WD.fillna(method='ffill',inplace=True)
    data['sin'] = np.sin(WD*np.pi/180)
    data['cos'] = np.cos(WD*np.pi/180)
    dat = []
    for i in range(len(data)):
        dat.append([complex(data['cos'].iloc[i],data['sin'].iloc[i])])
    dat = np.array(dat, dtype=complex)
    signal = dat[:,0]
    scales = np.logspace(0, 5, num=400, dtype=np.int32)
    fig, (ax) = plt.subplots(1, 1,figsize=(18,8))
    scg.cws(time,signal, scales,clim=(0,20),
            cbar= 'horizontal',cmap='inferno',cbarlabel='Amplitude (absCWT)',
            cbarkw={'aspect':45, 'pad':0.15,'shrink':0.5, 
                    'fraction':0.05,'ticks':[0,5,10,15,20,25,30]},
            ylabel="Period [hour]", xlabel='minute',yscale='log',ax=ax)
    y_tic = [1,2,4,8,12,16,24,32,64,128]
    ax.set_yticks(y_tic)
    ax.set_yticklabels(y_tic)
    m_day = [0,31,28,31,30,31,30,31,31,30,31,30]
    x_tic = np.array(m_day)*24
    x_tic2 = x_tic.copy()
    for i in range(len(x_tic)):
        x_tic2[i] = int(x_tic[i] + x_tic[:i].sum())
    base = data['DateTime'].iloc[0]
    mon = ['01','02','03','04','05','06','07','08','09','10','11','12']
    arr=np.array(["{}-{}".format(base.year,mon[i]) for i in range(len(mon))])
    ax.set_xticks(x_tic2)
    ax.set_xticklabels(arr)
    ax.set_ylim(1,y_tic[-1])
    ax.tick_params(axis="x", labelsize=18)
    ax.tick_params(axis="y", labelsize=18)
    ax.set_ylabel("Period [hour]",size=20)
    ax.set_xlabel("Time [month]",size=18)
    ax.set_title("Contunuous Wavelet Transform of Wind Direction ({})".format(year),size=20)
    plt.show()
