import json, asyncio, os
from multiprocessing.connection import wait
from cProfile import run
from http import server
import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord import FFmpegPCMAudio
import youtube_dl
import requests
import random
import time


with open('setting.json','r',encoding='utf8')as jfile:
	jdata=json.load(jfile)

class Music(Cog_Extension):
	@commands.command(pass_context=True)
	async def join(self,ctx):
		if (ctx.author.voice):
			channel = ctx.message.author.voice.channel
			voice = await channel.connect()
			source = FFmpegPCMAudio('E.wav')
			player = voice.play(source)


		else:
			await ctx.send("i can't find you")

	@commands.command(pass_context=True)
	async def leave(self,ctx):
		voice_client = ctx.guild.voice_client
		if (ctx.voice_client):
			await voice_client.disconnect()
			await ctx.send("bye~")
		else:
			await ctx.send("i am playing game!!")

	@commands.command(pass_context=True)
	async def joinE(self,ctx):
		
		if (ctx.author.voice):
			channel = ctx.message.author.voice.channel
			voice = await channel.connect()
			source = FFmpegPCMAudio('E.wav')
			player = voice.play(source)
			time.sleep(10)
			voice_client = ctx.guild.voice_client
			await voice_client.disconnect()


	# @commands.command(pass_context=True)
	# async def leave







def setup(bot):
	bot.add_cog(Music(bot))
