import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from datetime import datetime
from datetime import timedelta

def Shrink_Data(data,scale):
    dataA = data[['DateTime','WS95']].copy()
    Cosine = np.cos(data['WD95']*np.pi/180)
    Sine   = np.sin(data['WD95']*np.pi/180)

    dataA['Cos'] = Cosine
    dataA['Sin'] = Sine

    scale = scale
    ShrinkData = []
    for i in range(len(dataA)):
        replace = int(np.floor((dataA['DateTime'][i].minute)/scale))*scale
        ShrinkData.append(dataA['DateTime'][i].replace(minute=replace))
        if i%50000 ==0:
            print("Progress {}".format(i))
    print("Shrink Time")
    dataA['DateTime'] = ShrinkData
    dataA = dataA.groupby('DateTime').mean()
    print("Shrink Done")

    dataA['WD95n'] = np.arctan2(dataA['Sin'],dataA['Cos'])*180/np.pi
    #Export File
    dataA.reset_index(inplace=True,drop=False)
    #print("Now Exporting...")
    #dataA.to_excel("wind-unfiltered-{}min.xlsx".format(scale))
    #print("Export Done")
    print("--------------------------")
    return dataA