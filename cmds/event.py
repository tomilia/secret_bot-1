from itertools import count
from lib2to3 import refactor
import discord
from discord.ext import commands
from core.classes import Cog_Extension, Gloable_Data, Global_Func
from core.errors import Errors
import json
import datetime
import asyncio
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f"Hi{member.author.mention} , Welocme to **{member.guild.name}**👋🏻")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f"Noooo{member.author.mention} just dead in **{member.guild.name}**😵")

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword1 = jdata['randome_msg_1']
        keyword12 = random.choice(jdata['randome_msg_1'])
        keyword2 = ['hi', 'hello', 'Hi', 'Hello']
        keyword22 = random.choice(['hi', 'hello', 'Hi', 'Hello'])
        keyword = ['xyz', 'pen', 'pie', 'abc', 'Cazy', 'cazy', 'shutup', 'omg' , 'idk']
        keywordstart = ["start"]
        keyword123 = random.choice(['xyz', 'pen', 'pie', 'abc', 'Cazy', 'cazy', 'shutup', 'omg' , 'idk'])
        keyword3 = ['Parrot', 'Parrot_bot']
        keyword32 = random.choice(['Parrot', 'Parrot_bot'])
        random_msgs = jdata['randome_msg']
        random_msgs2 = random.choice(jdata['randome_msg'])
        random_memes = jdata['url_pic']
        random_memes2 = random.choice(jdata['url_pic'])
        if msg.content in keywordstart:
            people = msg.author.send
            await msg.reply(keyword123)
            await people("start")
        elif msg.content in keyword:
            await msg.reply(keyword12)
        elif msg.content in keyword1:
            await msg.reply(keyword22)
        elif msg.content in keyword2:
            await msg.reply(keyword32)
        elif msg.content in keyword3:
            await msg.reply(random_memes2)
        elif msg.content in random_memes:
            await msg.reply(random_msgs2)
        elif msg.content in random_msgs:
            await msg.reply(keyword123)


def setup(bot):
    bot.add_cog(Event(bot))
