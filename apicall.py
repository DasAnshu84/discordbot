import requests
import json
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as pl
import yfinance as yf
from datetime import datetime,timedelta

'''def get_data(stock,start_date,end_date):
    yf.pdr_override()
    for retries in range(0,5):
        try:
         df=pdr.get_data_yahoo(stock,start=start_date,end=end_date)
         return df['Adj Close']
        except:
            print("[ERROR]")
            print('yfinance JSONDecodeError')
        return []
    

quo = 'msft'
now = datetime.now()
old_year = now.year - 2
current_date=now.strftime("%Y-%m-%d")
current_date_arr = current_date.split('-')
old_date = str(old_year)+'-'+current_date_arr[1]+'-'+ current_date_arr[2]
print(f"new: {current_date}  old:{old_date}")
x=get_data(quo,old_date,current_date)
plot=pl.plot(x)
fig=plot.get_figure()
pl.show()'''
yesterday_datetime = datetime.now() - timedelta(days=1)

yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')

print(yesterday_date[4])