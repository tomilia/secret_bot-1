import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random, os, asyncio

intents=discord.Intents.all()
intents.members= True
intents.presences = True

with open('setting.json','r',encoding='utf8')as jfile:
	jdata=json.load(jfile)
	

# 讀取設定檔 load settings
bot = commands.Bot(command_prefix= jdata['Prefix'], 
owner_ids= jdata['Owner_id'])


# Bot完成啟動後事件
@bot.event
async def on_ready():
	print("Bot is online, ✔️")

# 載入cmds資料夾內所有cog
for Filename in os.listdir("./cmds"):
	if Filename.endswith(".py"):
		bot.load_extension(f'cmds.{Filename[:-3]}')



if __name__ == "__main__":
	bot.run(jdata['TOKEN'])
	