from itertools import count
from lib2to3 import refactor
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
	
	@commands.Cog.listener()
	async def on_raw_reaction_add(self, data):
		#判斷反應貼圖給予相對應的身份組
		#判斷反應反應信息是否為指定的訊息
		if data.message_id == 997525435313299558:
			if str(data.emoji) == '<:jail:997316329340162100>':
				guild = self.bot.get_guild(data.guild_id)#取得當前所在伺服器
				role = guild.get_role(997517745589600369)#取得伺服器內指定的身份組
				await data.member.add_roles(role)#給予該成員身份組
				await data.member.send(f"你取得了**{role}**身份組!")

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, data):
		#判斷反應貼圖給予相對應的身份組
		#判斷反應反應信息是否為指定的訊息
		if data.message_id == 997525435313299558: 
			if str(data.emoji) == '<:jail:997316329340162100>':
				guild = self.bot.get_guild(data.guild_id)#取得當前所在伺服器
				user = guild.get_member(data.user_id)#取得使用者
				role = guild.get_role(997517745589600369)#取得伺服器內指定的身份組
				await user.remove_roles(role)#移除該成員身份組
				await user.send(f"你移除了**{role}**身份組!")

	@commands.Cog.listener()
	async def on_message_delete(self, msg):
		counter = 1
		async for audilog in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete):
			if counter == 1:
				await msg.channel.send(audilog.user.name)
				counter += 1
			

		# await msg.channel.send("刪除訊息內容:" + str(msg.content))
		# await msg.channel.send("信息原本的作者:" + str(msg.author))


def setup(bot):
	bot.add_cog(Event(bot))