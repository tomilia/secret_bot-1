from tkinter import Menubutton
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime
import random

with open('setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

class Main(Cog_Extension):

    
    @commands.command()
    async def ping(self,ctx):
        await ctx.reply(f"{round(self.bot.latency*1000)}ms")

    @commands.command()
    async def hi(self,ctx):
        await ctx.send('hi:P')




    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="secret bot", description="my first discord bot !", color=0x28ddb0)
        embed.set_author(name="secret bot", icon_url="https://yt3.ggpht.com/Jc6PYgdUIVd2lWGKub6MECAIVbRjHdbzFhOq6nMjsh6uM1HkXVC3AipTIV7qtLVB0uoAUlCmUQ=s600-c-k-c0x00ffffff-no-rj-rp-mo")
        #embed.set_thumbnail(url="https://www.youtube.com/channel/UCBQifyXpKXmtzBzI_qK97rw/featured")
        embed.add_field(name="開發者 Developers", value="harryxd_x#0211 (<@!823743982680801281>)", inline=False)
        embed.add_field(name="版本 Version", value="0.7.1 b", inline=False)
        embed.add_field(name="Prefix", value=";", inline=False)
        embed.set_footer(text="Made with ❤")
        await ctx.send(embed=embed)


    # @commands.command()
    # async def info(self,ctx):
    #     embed=discord.Embed(title="Bot info", color=0x007bff,
    #     timestamp = datetime.datetime.utcnow())
    #     embed.set_author(name="secret bot", icon_url="https://yt3.ggpht.com/Jc6PYgdUIVd2lWGKub6MECAIVbRjHdbzFhOq6nMjsh6uM1HkXVC3AipTIV7qtLVB0uoAUlCmUQ=s600-c-k-c0x00ffffff-no-rj-rp-mo")
    #     embed.add_field(name="ping", value=f"{round(self.bot.latency*1000)}ms", inline=False)
    #     await ctx.send(embed=embed)

        #await ctx.message.delete()

    @commands.command()
    async def 信息(self,ctx):
        embed=discord.Embed(title="Bot 信息", color=0x007bff,
        timestamp = datetime.datetime.utcnow())
        embed.set_author(name="secret的神奇小幫手", icon_url="https://yt3.ggpht.com/Jc6PYgdUIVd2lWGKub6MECAIVbRjHdbzFhOq6nMjsh6uM1HkXVC3AipTIV7qtLVB0uoAUlCmUQ=s600-c-k-c0x00ffffff-no-rj-rp-mo")
        embed.add_field(name="延遲", value=f"{round(self.bot.latency*1000)}毫秒", inline=False)
        await ctx.send(embed=embed)
    
    #embed = discord.Embed(title="All star", description="All star character", color=0x007bff,
    #timestamp = datetime.datetime.utcnow())
    #embed.set_author(name="secret bot", icon_url="https://yt3.ggpht.com/Jc6PYgdUIVd2lWGKub6MECAIVbRjHdbzFhOq6nMjsh6uM1HkXVC3AipTIV7qtLVB0uoAUlCmUQ=s600-c-k-c0x00ffffff-no-rj-rp-mo")
    #embed.set_thumbnail(url="https://i.pinimg.com/564x/6a/17/03/6a17031bd6d1def14da3db7840ca0698.jpg")
    #embed.add_field(name="5*", value="nothing", inline=False)
    #embed.add_field(name="4*", value="nothing,nothing", inline=False)
    #embed.add_field(name="3*", value="nothing,nothing,nothing", inline=False)
    #embed.add_field(name="money", value="nothing,nothing,nothing,nothing,nothing", inline=True)
    #embed.set_footer(text="nothing:P")
    #await ctx.send(embed=embed)

    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def delete(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)


    @commands.command()
    async def random_grop(self,ctx):
        online = []
        for member in ctx.guild.members:
            if str(member.status) == 'online' and member.bot == False or str(member.status) == 'idle' and member.bot == False:
                online.append(member.name)


        random_online = random.sample(online, k=4)#--20 #how many people in all team

        for squad in range(2):
            a = random.sample(random_online, k=2)#--5 #how many people in 1 team
            await ctx.send(f"Grop{squad+1}:" + str(a))
            for name in a:
                random_online.remove(name)

        
    @commands.group()
    async def codetest(self, ctx):
        pass

    @codetest.command()
    async def python(self, ctx):
        await ctx.send("Python")
        
    @codetest.command()
    async def javascript(self, ctx):
        await ctx.send("javascript")
        
    @codetest.command()
    async def cpp(self, ctx):
        await ctx.send("C++")
        

    @commands.command()
    async def cmdA(self, ctx, num: float):
        await ctx.send(num)

    @commands.command()
    async def cmdB(self, ctx, num: float):
        await ctx.send(num)

            
        
def setup(bot):
    bot.add_cog(Main(bot))
    