import discord
import random
from discord.ext import commands

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # !가위바위보
    @commands.command()
    async def 가위바위보(ctx, user: str):
        RCP = ["가위", "바위", "보"]
        bot = random.choice(RCP)
        result = RCP.index(user) - RCP.index(bot)

        if result == 0:
            await ctx.send(f"[ 숭이는 {bot}! ]\n🙊 비겼숭;; 🙊")
        elif result == 1 or result == -2:
            await ctx.send(f"[ 숭이는 {bot}! ]\n🙈 ㅗ 🙈")
        else:
            await ctx.send(f"[ 숭이는 {bot}! ]\n🙉 낵아 이겼숭~! 🙉")

def setup(bot):
    bot.add_cog(Game(bot))