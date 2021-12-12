import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.members= True

bot = commands.Bot(command_prefix=";",intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(919426769923227658)
    await channel.send(F"{member}join!")
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(919423448168681472)
    await channel.send(F"{member}leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(F"{round(bot.latency*1000)}(ms)")
bot.run('OTE5MTk5NzI5NjAxMTEwMDQ3.YbSVdQ.5zKzuanvpUKANIx3MJDdmp53Yxk')
    