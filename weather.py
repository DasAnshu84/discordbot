import discord
import requests
import json

intents = discord.Intents.default()
intents.presences = True  
intents.message_content = True

client = discord.Client(intents = intents)

def get_weather(city):
    response=requests.get(f"http://api.weatherapi.com/v1/current.json?key=b56ac9b202d64dd8a0c114331231805&q={city}&aqi=no")
    data=response.json()

    if response.status_code == 200:
        weather_data=data["current"]["condition"]["text"]
        temp=data["current"]["temp_c"]

        weather_info = f"Location : {city}\n"
        weather_info += f"{weather_data}\n"
        weather_info += f"Temperature: {temp}\n"
        return weather_info
    else:
        return None

    


@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith('!weather'):
        city=message.content[9:]
        weather_data=get_weather(city)
        
        if weather_data:
         await message.channel.send(weather_data)
        else:
          await message.channel.send("Error fetching")

client.run('MTEwNjgzNjQzNzIyNTE4OTQ0Ng.G6xTRq.sQeu0YinYc_ggJ2wyUUqX32UG4Qi0jDPVsognI')