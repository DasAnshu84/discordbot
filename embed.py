import discord
import requests
import json

intents = discord.Intents.default()
intents.presences = True  
intents.message_content = True

client = discord.Client(intents = intents)



@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content.startswith("!embed"):
        embed = discord.Embed(title="This is an embed", description="This is the embed's description.", color=discord.Color.red())
        embed.add_field(name="This is a field", value="This is the field's value.", inline=False)
        await message.channel.send(embed=embed)

client.run('MTEwNjgzNjQzNzIyNTE4OTQ0Ng.GcXHv4.33r5gEfwILvnzlNAlfL-teB9BMmW1AKeerGdP0')