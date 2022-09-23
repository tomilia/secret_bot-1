from itertools import count
from lib2to3 import refactor
import discord
from discord.ext import commands
from core.classes import Cog_Extension, Gloable_Data ,Global_Func
from core.errors import Errors
import json, datetime, asyncio
import random

with open('setting.json','r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

class Event(Cog_Extension):
	@commands.Cog.listener()
	async def on_member_join(self,member):
		channel = self.bot.get_channel(int(jdata['Welcome_channel']))
		await channel.send(f"Hi{member.author.mention} , Welcome to **{member.guild.name}**👋🏻")

	@commands.Cog.listener()
	async def on_member_remove(self,member):
		channel = self.bot.get_channel(int(jdata['Leave_channel']))
		await channel.send(f"Noooo{member.author.mention} just dead in **{member.guild.name}**😵")

	@commands.Cog.listener()
	async def on_message(self,msg):
		keyword1 =jdata['randome_msg_1']
		keyword2 =['hi','hello','Hi','Hello']
		keyword =['apple','pen','pie','abc']
		keyword3 =['Parrot','Parrot_bot']
		random_msgs = random.choice(jdata['randome_msg'])
		random_msgs_1 = random.choice(jdata['randome_msg_1'])
		if msg.content in keyword1 and msg.author.bot == False and msg.author != self.bot.user:
			await msg.channel.send(random_msgs_1)
			if random_msgs_1 == msg.content:
				await msg.reply("曾志偉:\"打和!!!!\"")
		elif msg.content in keyword and msg.author != self.bot.user:
			await msg.channel.send(random_msgs)
		elif msg.content in keyword2 and msg.author != self.bot.user:
			await msg.reply(f"{msg.author.mention} \nhi welocme to **{msg.guild.name}** server {(random_msgs)}")
		elif msg.content in keyword3 and msg.author != self.bot.user:
			await msg.reply(Global_Func.code(lang="diff",msg = f"-{msg.author.name} \n-i am not fucking Parrot"))
		# lang diff = red ,css[] = orange , fix = yellow , diff+ = green , css“ = light green , ini[ = blue

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
		if data.message_id == 1022921722971824158:
			if str(data.emoji) == ':white_check_mark: ':
				guild = self.bot.get_guild(data.guild_id)#取得當前所在伺服器
				role = guild.get_role(1022920579776512020)#取得伺服器內指定的身份組
				await data.member.add_roles(role)#給予該成員身份組
				await data.member.send(f"你取得了**{role}**身份組!")

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, data):
		#判斷反應貼圖給予相對應的身份組
		#判斷反應反應信息是否為指定的訊息
		if data.message_id == 1022921722971824158: 
			if str(data.emoji) == ':white_check_mark: ':
				guild = self.bot.get_guild(data.guild_id)#取得當前所在伺服器
				user = guild.get_member(data.user_id)#取得使用者
				role = guild.get_role(1022920579776512020)#取得伺服器內指定的身份組
				await user.remove_roles(role)#移除該成員身份組
				await user.send(f"你移除了**{role}**身份組!")

	@commands.Cog.listener()
	async def on_message_delete(self, msg):
		counter = 1
		async for audilog in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete):
			if counter == 1:
				# await msg.channel.send(audilog.user.name)
				counter += 1
			

		# await msg.channel.send("刪除訊息內容:" + str(msg.content))
		# await msg.channel.send("信息原本的作者:" + str(msg.author))


def setup(bot):
	bot.add_cog(Event(bot))