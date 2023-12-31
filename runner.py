from discord.ext import commands
import builtins
from os import getenv

bot = commands.Bot('@')
builtins.bot = bot

@bot.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    await bot.send_message(channel, "pong")

bot.run("TOKEN")