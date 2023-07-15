import discord
import requests
import json
import random

intents = discord.Intents.default()
intents.presences = True  
intents.message_content = True

client = discord.Client(intents = intents)

sad_words=["sad","depressed","demotivated","unhappy","angry","dukhi","depressing","miserable"]

random_encouragements=[
    "Hang in there.",
    "You are a great person",
    "Tu karlega.Bharosa Rakh",
    "Uparwala dekhraha hai.Chalte jaa"
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data=response.json()

    if response.status_code == 200:
        quote=data[0]['q'] + ' -' + data[0]['a']
    
    return (quote)


@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith('!inspire'):
        quote=get_quote()
        await message.channel.send(quote)
    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(random_encouragements))

client.run('MTEwNzc0NzU2OTg3NjA4Njc4NA.GZJM4b.Ncte3TrzH0-an5ZhguJ669trqq1-ULKlqxTTJw')