import os
import discord
import sys
from dotenv import load_dotenv

import re
from num2words import num2words

load_dotenv()
token = str(os.getenv("TOKEN"))

intents = discord.Intents.all()
intents.members = True
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
	print(f"{bot.user} is ready and online!")
	# activity = discord.CustomActivity(name="bored")
	# await bot.change_presence(activity=activity)

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
	await ctx.respond("Hey!")

@bot.slash_command(name="goodbye", description="Say goodbye to the bot")
async def hello(ctx):
	await ctx.respond("Goodbye!")
	sys.exit

# @bot.slash_command(name="add_show", description="add a new show to the current list")
# async def addShow(
# 	ctx: discord.ApplicationContext,
# 	title: discord.Option(str),
# 	status: discord.Option(str, choices=["planned", "watching", "completed"])
# ):
# 	newItem = [showsObject.currentID, title, status, 0, 0, 0, 0, 0]
# 	showsObject.addShow(newItem)
# 	await ctx.channel.send("Added " + title + " as " + status + "👍")

bot.run(os.getenv('TOKEN'))