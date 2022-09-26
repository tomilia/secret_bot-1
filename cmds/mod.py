from http import server
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


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def kick(self, ctx, member:discord.Member, *,reason=None):
		await member.kick(reason=reason)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def ban(self,ctx, member:discord.Member, *,reason="No reson"):
		role = ctx.guild.get_role(1022902918434783362)#取得伺服器內指定的身份組
		await member.add_roles(role)#給予該成員身份組
		await member.send(f"You get **{role}** because **{reason}**")

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def unban(self,ctx, member:discord.Member, *,reason="No reson"):
		role = ctx.guild.get_role(1022902918434783362)#取得伺服器內指定的身份組
		await member.remove_roles(role)#給予該成員身份組
		await member.send(f"we clear your **{role}** because **{reason}**")
		

	@commands.command(pass_context = True)
	@commands.has_permissions(administrator=True)
	async def mute(self,ctx, member:discord.Member, *,reason="No reson"):
		role = ctx.guild.get_role(1022901234530791464)#取得伺服器內指定的身份組
		await member.add_roles(role)#給予該成員身份組
		await member.send(f"You get **{role}** because **{reason}**")
		

	@commands.command(pass_context = True)
	@commands.has_permissions(administrator=True)
	async def unmute(self,ctx, member:discord.Member, *,reason= "No reson"):
		role = ctx.guild.get_role(1022901234530791464)#取得伺服器內指定的身份組
		await member.remove_roles(role)#給予該成員身份組
		await member.send(f"we clear your **{role}** because **{reason}**")

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
	async def change2(self, ctx, type: str, *, content: str):#, *, content: str):
		activity = discord.Game(name="!help")
		typeList = {
			"game": 1,
			"streaming": 2,
			"listening": 3,
			"watching": 4
		}
		if(typeList[content] == 4){
			watching = discord.Activity(type=discord.ActivityType.watching, name="a movie")
			await this.bot.change_presence(activity=watching)
			await ctx.send(content=Global_Func.code(lang='fix', msg=f"Change done. \nType:watching"), delete_after=5.0)
		}
		



def setup(bot):
   bot.add_cog(Mod(bot))