# List
m_day = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['01','02','03','04','05','06','07','08','09','10',
      '11','12','13','14','15','16','17','18','19','20',
      '21','22','23','24','25','26','27','28','29','30','31']
mon = ['01','02','03','04','05','06',
       '07','08','09','10','11','12']
mon_name =['January'  ,'February','March'   ,'April' ,
           'May'      ,'June'   ,'July'    ,'August',
           'September','October','November','December']
# Dict
mon_dic = {1:'Jan'  ,2 :'Feb' ,3 :'Mar' ,4 :'Apr',
            5:'May'  ,6 :'Jun' ,7 :'Jul' ,8 :'Aug',
            9:'Sep'  ,10:'Oct' ,11:'Nov' ,12:'Dec'}

# season
seasons = [(month%12 + 3)//3 for month in range(1, 13)]
month_to_season = dict(zip(range(1,13), seasons))
#df['Season']= df['Month'].apply(lambda x:month_to_season[x])
Season_dict = {1:'Spring',2:'Summer',3:'Autumn',4:'Winter'}