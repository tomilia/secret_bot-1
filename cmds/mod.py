import types
import discord
from discord.ext import commands
from core.classes import Cog_Extension, Global_Func
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Mod(Cog_Extension):

	@commands.command(aliases=['cc'])
	@commands.has_permissions(administrator=True)
	async def purge(self, ctx, num: int, reason=None):
		'''清理指定數量訊息'''
		await ctx.channel.purge(limit=num + 1)
		
		levels = {
			"1": "非對應頻道內容",
			"2": "不雅用詞",
			"3": "刷屏",
			"4": "沒有用或有害的連結"	
		}

		if reason is not None:
			if reason in levels.keys():
				await ctx.send(Global_Func.code(lang='fix', msg=f'已清理 {num} 則訊息.\nReason: {levels[reason]}'))
			else:
				await ctx.send(Global_Func.code(lang='fix', msg=f'已清理 {num} 則訊息.\nReason: {reason}'))
		else:
			await ctx.send(content=Global_Func.code(lang='fix', msg=f'已清理 {num} 則訊息.\nReason: {reason}'), delete_after=5.0)

	@commands.has_permissions(administrator=True)
	@commands.command()
	async def change(self, ctx, *, content: str ,type=None,url : str =None):
		game = discord.Game(content)
		# streaming = discord.Streaming(name=content,url=url)
		watching = discord.ActivityType.watching(content)
		listening = discord.ActivityType.listening(content)

		Choose = {
			"game",
			"streaming",
			"listening",
			"watching"
		}
		if type is not None:
			if type in Choose.keys():
				if type == game():
					await ctx.change_presence(status=discord.Status.idle, activity=game)
					await ctx.send(lang='fix',msg=f"Change done. \nType:{Choose[type]}")
				# elif type == streaming():
				# 	await ctx.change_presence(status=discord.Status.idle, activity=streaming)
				# 	await ctx.send(lang='fix',msg=f"Change done. \nType:{Choose[type]}")	
				elif type == listening():
					await ctx.change_presence(status=discord.Status.idle, activity=watching)
					await ctx.send(lang='fix',msg=f"Change done. \nType:{Choose[type]}")
				else:
					await ctx.change_presence(status=discord.Status.idle, activity=listening)
					await ctx.send(lang='fix',msg=f"Change done. \nType:{Choose[type]}")
			else:
				await ctx.change_presence(status=discord.Status.idle, activity=game)
				await ctx.send(lang='fix',msg=f"type can't found\n Change done. \nType:game")
		else:
			await ctx.change_presence(status=discord.Status.idle, activity=game)
			await ctx.send(lang='fix',msg=f"No type\n Change done. \nType:game")

	@commands.command()
	async def change2(self, ctx):#, *, content: str):
		activity = discord.Game(name="!help")
		await ctx.change_presence(status=discord.Status.idle, activity=activity)




def setup(bot):
   bot.add_cog(Mod(bot))