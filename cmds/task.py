import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


        #async def interval():
        #    await self.bot.wait_until_ready()
        #    self.channel = self.bot.get_channel(879337317846896721)
        #    while not self.bot.is_closed():
        #        await self.channel.send("Hi i'm running!")
        #        await asyncio.sleep(5)#second
        #
        #self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(879337317846896721)
            while not self.bot.is_closed():
                pass
        #self.bg_task = self.bot.loop.create_task(interval())


    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')

    @commands.command()
    async def set_time(self, ctx, time):
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)






def setup(bot):
    bot.add_cog(Task(bot))