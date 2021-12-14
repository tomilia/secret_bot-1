import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime

with open('setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

class Main(Cog_Extension):

    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}ms")

    @commands.command()
    async def hi(self,ctx):
        await ctx.send('hi:P')

    @commands.command()
    async def em(self,ctx):
        embed=discord.Embed(title="All star", description="All star character", color=0x007bff,
        timestamp = datetime.datetime.utcnow())
        embed.set_author(name="harryxd_x", icon_url="https://i.pinimg.com/564x/6a/17/03/6a17031bd6d1def14da3db7840ca0698.jpg")
        embed.set_thumbnail(url="https://i.pinimg.com/564x/6a/17/03/6a17031bd6d1def14da3db7840ca0698.jpg")
        embed.add_field(name="5*", value="nothing", inline=False)
        embed.add_field(name="4*", value="nothing,nothing", inline=False)
        embed.add_field(name="3*", value="nothing,nothing,nothing", inline=False)
        embed.add_field(name="money", value="nothing,nothing,nothing,nothing,nothing", inline=True)
        embed.set_footer(text="nothing:P")
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def delete(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)

            
        
def setup(bot):
    bot.add_cog(Main(bot))
    