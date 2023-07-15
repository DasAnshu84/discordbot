import discord
import requests
import json
import pandas as pd
import matplotlib.pyplot as pl
from pandas_datareader import data as pdr
import yfinance as yf
from datetime import datetime,timedelta

from discord.ext import commands
intents = discord.Intents.default()
intents.presences = True
intents.message_content = True

client = discord.Client(intents = intents)

def get_data1(stock,start_date,end_date):
    yf.pdr_override()
    for retries in range(0,5):
        try:
         df=pdr.get_data_yahoo(stock,start=start_date,end=end_date)
         return df['Adj Close']
        except:
            print("[ERROR]")
            print('yfinance JSONDecodeError')
        return []
    
def get_chart(quo):
   now = datetime.now()
   old_year = now.year - 2
   current_date=now.strftime("%Y-%m-%d")
   current_date_arr = current_date.split('-')
   old_date = str(old_year)+'-'+current_date_arr[1]+'-'+ current_date_arr[2]
   data=get_data1(quo,old_date,current_date)
   pl.clf()
   plot=data.plot(title=f'Stock Price of {quo} over 2 years')
   fig=plot.get_figure()
   filename='output.png'
   fig.savefig(filename)
   return filename


def get_data(sign):
    

    response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={sign}&interval=5min&apikey=UX9AFPO620XB8FXG")
    data=response.json()

    if response.status_code == 200:
        last_refreshed=data["Meta Data"]["3. Last Refreshed"]
        open=data["Monthly Time Series"][last_refreshed]["1. open"]
        high=data["Monthly Time Series"][last_refreshed]["2. high"]
        low=data["Monthly Time Series"][last_refreshed]["3. low"]
        close=data["Monthly Time Series"][last_refreshed]["4. close"]
    
        stock_info=f"Symbol  :          {sign}\n"
        stock_info +=f"Open  :          {open}\n"
        stock_info +=f"High  :           {high}\n"
        stock_info +=f"Low   :            {low}\n"
        stock_info +=f"Close :          {close}\n"
        stock_info +=f"Last Refreshed:  {last_refreshed}\n"
    return (stock_info)


@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content.startswith("!check"):
         sign=message.content[7:]
         stock_info=get_data(sign)

         if stock_info:
          await message.channel.send(stock_info)
         else:
          await message.channel.send("Error fetching")

    if message.content.startswith("!chart"):
         quo=message.content[7:]
         filename=get_chart(quo)
         
         await message.channel.send(file=discord.File(filename))
        

client.run('MTEwNjgzNjQzNzIyNTE4OTQ0Ng.GcXHv4.33r5gEfwILvnzlNAlfL-teB9BMmW1AKeerGdP0')