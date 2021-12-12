import discord
from discord.ext import commands
import json
import random


intents=discord.Intents.default()
intents.members= True

with open('setting.json','r',encoding='utf8')as jFile:
    jdata=json.load(jFile)


bot = commands.Bot(command_prefix=";",intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online")


@bot.command()
async def photo(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file= random_pic)

@bot.command()
async def memes(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(F"{member}join!")
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(F"{member}leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(F"{round(bot.latency*1000)}(ms)")
bot.run(jdata['TOKEN'])
    