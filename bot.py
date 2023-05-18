import discord

from discord.ext import commands
intents = discord.Intents.default()
intents.presences = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
names=["compliment_me","hello","kya_karu","anshu","parthiv","pardu","ananya","ankit","shubhavi","roshan","hotel","ask"]
@bot.command()
async def list(message):
    for x in names:
     await message.send(x)

@bot.command()
async def compliment_me(message):
    await message.send('You are smart and  I know it')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hey, {ctx.author.name}!')
@bot.command()
async def kya_karu(message):
    await message.send('Sabse pehle lambi saans loh aur thoda chill karo yaar sab hojaiga')
@bot.command()
async def anshu(ctx):
    await ctx.send('overrated af or shall I say "Is he seriously rated?"')
@bot.command()
async def parthiv(message):
    await message.send('Incorrect spelling!.Try "!pardu"')
@bot.command()
async def pardu(ctx):
    await ctx.send('Why spoil your day')
@bot.command()
async def ananya(message):
    await message.send('so called pyaar se marne wali')
@bot.command()
async def ankit(ctx):
    await ctx.send('wo toh sidha hai')
@bot.command()
async def shubhavi(message):
    await message.send('SSS-Smart Strict Shubhavi')
@bot.command()
async def okay(ctx):
    await ctx.send('Kuch okay nahi hai.Beware!')
@bot.command()
async def roshan(message):
    await message.send('Bolo zubaan canceriya')
@bot.command()
async def hotel(message):
    await message.send('Trivago')
@bot.command()
async def ask(ctx):
    await ctx.send('Melody itni chocolaty kyun hoti hain?')




    

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
@bot.event
async def on_member_update(before, after):
    if before.status != discord.Status.online and after.status == discord.Status.online:
        guild = after.guild
        channel = discord.utils.get(guild.text_channels, name="general")  # Replace "general" with the desired channel name
        if channel:
            await channel.send(f'Welcome {after.mention} back online in {guild.name}!')

bot.run('MTEwNzc0NzU2OTg3NjA4Njc4NA.GwkDWH.s1lluyKIbiagp6fHb8lCp_lnDyb8O1L_F5VqiM')