import discord
from discord.ext import commands
from core.classes import Cog_Extension, Gloable_Data
from core.errors import Errors
import json, datetime, asyncio

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(F"{member}join!👋🏻")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(F"{member}leave!👋🏻")

    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword =['apple','pen','pie','abc']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('apple')


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        '''指令錯誤觸發事件'''
        Gloable_Data.errors_counter += 1
        error_command = '{0}_error'.format(ctx.command)
        if hasattr(Errors, error_command):  # 檢查是否有 Custom Error Handler
            error_cmd = getattr(Errors, error_command)
            await error_cmd(self, ctx, error)
            return
        else:  # 使用 Default Error Handler
            await Errors.default_error(self, ctx, error)

def setup(bot):
    bot.add_cog(Event(bot))