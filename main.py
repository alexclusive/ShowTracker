import os
import discord
from dotenv import load_dotenv

import re
from num2words import num2words

from shows import shows

load_dotenv()
token = str(os.getenv("TOKEN"))

intents = discord.Intents.all()
intents.members = True
bot = discord.Bot(intents=intents)

showsObject = shows()

@bot.event
async def on_ready():
	print(f"{bot.user} is ready and online!")
	# activity = discord.CustomActivity(name="bored")
	# await bot.change_presence(activity=activity)
	showsObject.updateShows("./assets/shows.txt")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
	await ctx.respond("Hey!")

@bot.slash_command(name="reset_show_list")
async def resetShowList(ctx):
	showsObject.clearFile()

@bot.slash_command(name="add_show", description="add a new show to the current list")
async def addShow(
	ctx: discord.ApplicationContext,
	title: discord.Option(str),
	status: discord.Option(str, choices=["planned", "watching", "completed"])
):
	newItem = [showsObject.currentID, title, status, 0, 0, 0, 0, 0]
	showsObject.addShow(newItem)
	await ctx.channel.send("Added " + title + " as " + status + "👍")

bot.run(os.getenv('TOKEN'))