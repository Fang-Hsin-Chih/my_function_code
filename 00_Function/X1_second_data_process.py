import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels
import datetime
import re
from datetime import datetime
from datetime import timedelta

day = ['01','02','03','04','05',
      '06','07','08','09','10',
      '11','12','13','14','15',
      '16','17','18','19','20',
      '21','22','23','24','25',
      '26','27','28','29','30','31']
mon = ['01','02','03','04','05','06',
       '07','08','09','10','11','12']
m_day = [31,28,31,30,31,30,31,31,30,31,30,31]
col = ['RecordTime', 'WS10', 'WS30', 'WS50', 'WS95A', 'WS95B', 'WD10', 'WD30', 'WD50', 'WD95']

def Convert_Nan(data,col):
    dataC = data.copy()
    dataC = dataC.replace('0',np.nan)
    dataC = dataC.replace('-999.00',np.nan)
    dataC = dataC.replace('-999.0',np.nan)
    dataC = dataC.replace('-999',np.nan)
    dataC = dataC.replace('NAN', np.nan)
    dataC = dataC.replace('NA', np.nan)
    dataC = dataC.replace('N', np.nan)
    dataC = dataC.replace('', np.nan)
    dataC = dataC.replace('-',np.nan)
    
    dataC.dropna(how='all',inplace=True)
    dataC.reset_index(drop=True, inplace=True)
    dataC.fillna(-999,inplace=True)
    for i in col[1:]:
        dataC[i] = dataC[i].astype('float')
    
    dataC[col[0]] = pd.to_datetime(dataC[col[0]])
    dataC = dataC.replace(-999,np.nan)
    return dataC

def Direction_Devide(data,Height):
    Cosine = np.cos(data['WD{}'.format(Height)]*np.pi/180)
    Sine   = np.sin(data['WD{}'.format(Height)]*np.pi/180)
    return Sine,Cosine

def read_1sec_data_and_save_to_each_month(year):
    for n in range(len(mon)):
        m = n
        #READ DATA
        data_path = 'D:/data/{}{}/'.format(year,mon[m])
        file_name = 'ChanghuRawW_{}{}.txt'.format(year,mon[m])
        df = pd.read_table(data_path + file_name,skiprows=15,encoding='gb2312',index_col=0)
        print("{}-{}, Import Done".format(year,mon[m]))

        #EXTRACT DATA FILE
        df2  = df.copy()
        df2.reset_index(inplace=True)
        col2 = df2.columns[0]
        df2  =df2[df2.columns[0]].str.split(',',expand=True) 
        df01 = pd.DataFrame(df2).copy()

        #SET COLUMN'S NAME
        col2  =re.split('; |, |\*|\n',col2)
        df01.columns = col
        print(col2)
        print("Rename Columns To: ")
        print(col)
        #CHANGE TYPE AND DROP NA
        df01 = Convert_Nan(df01,col)
        print("FORMAT Converted")
        #GROUPING SECONDS To MINUTES level
        Sec = []
        df02 = df01.copy()
        for i in range(len(df02)):
            Sec.append(df02[col[0]][i])
        df02['DateTime'] = Sec
        data_1sec = df02.groupby('DateTime').mean()
        print("{}-{}, Preprocessing Done".format(year,mon[m]))
    
        # Reindex
        start_date = "{}-{}-01".format(year,mon[m])
        duration = m_day[m]
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        stop_date  = start_date+timedelta(days=duration)
        idx = pd.period_range(start=start_date, end=stop_date, freq='S')
        #Fill Empty Cell
        data_D = data_1sec.reindex(idx, fill_value=np.nan)
        data_D.index = data_D.index.to_timestamp()
        df_F = pd.concat([data_D,data_1sec])
        df_F = df_F.groupby(df_F.index).mean()
        print(df_F.head())
        print("Now Exporting...")
        df_F.to_csv('wind_{}-{}-1sec.csv'.format(year,mon[m]))
    print("{}-{}, Export Done".format(year,mon[m]))
    print("--------------------------")



def read_1sec_data_year2017(year=2017):
    for n in range(len(mon)):
        m = n
        #READ DATA
        data_path = 'D:/data/{}00/'.format(year)
        file_name = 'ChanghuRawW_{}{}.txt'.format(year,mon[m])
        df = pd.read_table(data_path + file_name,skiprows=15,encoding='gb2312',index_col=0)
        print("{}-{}, Import Done".format(year,mon[m]))

        #EXTRACT DATA FILE
        df2  = df.copy()
        df2.reset_index(inplace=True)
        col2 = df2.columns[0]
        df2  =df2[df2.columns[0]].str.split(',',expand=True) 
        df01 = pd.DataFrame(df2).copy()

        #SET COLUMN'S NAME
        col2  =re.split('; |, |\*|\n',col2)
        df01.columns = col
        print(col2)
        print("Rename Columns To: ")
        print(col)
        #CHANGE TYPE AND DROP NA
        df01 = Convert_Nan(df01,col)
        print("FORMAT Converted")
        #GROUPING SECONDS To MINUTES level
        Sec = []
        df02 = df01.copy()
        for i in range(len(df02)):
            Sec.append(df02[col[0]][i])
        df02['DateTime'] = Sec
        data_1sec = df02.groupby('DateTime').mean()
        print("{}-{}, Preprocessing Done".format(year,mon[m]))
    
        # Reindex
        start_date = "{}-{}-01".format(year,mon[m])
        duration = m_day[m]
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        stop_date  = start_date+timedelta(days=duration)
        idx = pd.period_range(start=start_date, end=stop_date, freq='S')
        #Fill Empty Cell
        data_D = data_1sec.reindex(idx, fill_value=np.nan)
        data_D.index = data_D.index.to_timestamp()
        df_F = pd.concat([data_D,data_1sec])
        df_F = df_F.groupby(df_F.index).mean()
        print(df_F.head())
        print("Now Exporting...")
        df_F.to_csv('wind_{}-{}-1sec.csv'.format(year,mon[m]))
    print("{}-{}, Export Done".format(year,mon[m]))
    print("--------------------------")


def Concat_whole_year(year): 
    data_1sec = pd.DataFrame()
    for n in range(len(mon)):
        m = n

        #READ DATA
        data_path = 'C:/0_Academy/Anaconda/WindPower/Wind_data/1. windspeed/sec/'
        file_name = 'wind_{}-{}-1sec.csv'.format(year,mon[m])
        df   = pd.read_csv(data_path +file_name)
        print("{}-{}, Import Done".format(year,mon[m]))
        df.rename(columns={'Unnamed: 0':'DateTime'}, inplace=True)
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        logicM = (df["DateTime"].apply(lambda x: x.month))==(m+1)
        new_data = df[logicM].copy()
    
        #Concat whole year data
        print("Now CONCAT ing")
        data_1sec = pd.concat([data_1sec,new_data])
        print("{}-{} CONCAT DONE".format(year,mon[m]))
        print("-------------------------------------------")
    print("{} Done".format(year))

    #Exporting
    data_1sec = data_1sec.groupby('DateTime').mean()
    data_1sec.to_csv("ALL_wind_{}-1sec.csv".format(year))
    return data_1sec

