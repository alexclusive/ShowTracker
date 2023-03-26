import os
import discord
from dotenv import load_dotenv

from shows import shows

load_dotenv()
token = str(os.getenv("TOKEN"))
bot = discord.Bot()

showsObject = shows()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    activity = discord.CustomActivity(name="bored")
    await bot.change_presence(activity=activity)
    showsObject.updateShows("./assets/shows.txt")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(os.getenv('TOKEN'))