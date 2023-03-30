import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Done')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command(name="hello")
async def _hello(ctx):
    await ctx.send("{}, 안녕하숭~!".format(ctx.author.mention))

bot.run('MTA5MDA4OTE5NjIwMDM5NDgyMw.GiWGwl.oPUxk3rD2kkdDooTHh_UBNmjqVUdJJZ-lnsCpc')
