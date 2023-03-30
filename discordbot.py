import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# 봇 상태 설정
@bot.event
async def on_ready():
    print('Done')

    #await bot.change_presence(status=discord.Status.online) #온라인
    await bot.change_presence(status=discord.Status.idle)  # 자리비움
    #await bot.change_presence(status=discord.Status.dnd) #다른 용무 중
    #await bot.change_presence(status=discord.Status.offline) #오프라인

    #await bot.change_presence(activity=discord.Game(name="개발"))
    await bot.change_presence(activity=discord.Game(name="딴 짓"))

# 멤버 추가될 때 인사
@bot.event
async def on_member_join(member):
    msg = "안녕하숭~"
    await member.send(msg)
    channel = bot.get_channel('1090085600201285654')
    await channel.send(msg)

# !help
@bot.command(aliases = ['HELP', '도움'])
async def embed(ctx):
    embed = discord.Embed(title="🙈 도움숭이 🙉", description="도움말 임니당~", color=0x62c1cc)
    embed.add_field(name="!hello", value="인사숭이 🐒", inline=False)
    embed.add_field(name="!가위바위보", value="가위바위보숭이 ✊", inline=False)
    await ctx.send(embed = embed)
    # await msg.add_reaction("🐒")
    # await msg.add_reaction("✊")

# !hello
@bot.command(name = "hello")
async def _hello(ctx):
    await ctx.send("{}, 안녕하숭~!".format(ctx.author.mention))


####################### game ######################

# !가위바위보
@bot.command()
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



###################### 숭숭 컬렉션 ######################

# 숭이 명령어 모음
@bot.command(aliases=['숭', '단축어'])
async def soong_help(ctx):
    embed = discord.Embed(title="🙈 숭이 명령어 모음 🙉", description="느낌표를 붙여주숭 ‼️", color=0x62c1cc)
    embed.add_field(name=" 메롱하는 숭이", value="➡️ 메롱", inline=True)
    embed.add_field(name=" 고백하는 숭이", value="➡️ 고백, 사귀자", inline=True)
    embed.add_field(name=" 미안한 숭이", value="➡️ 미안, 미안해", inline=True)
    embed.add_field(name=" 숭-하", value="➡️ 숭하, 하이, ㅎㅇ, 안녕", inline=True)
    embed.add_field(name=" 숭이팅하는 숭이", value="➡️ 화이팅, ㅎㅇㅌ, 숭이팅", inline=True)
    embed.add_field(name=" 대답하는 숭이", value="➡️ 웅, ㅇㅇ, ㅇ", inline=True)
    embed.add_field(name=" 머하냐고 묻는 숭이", value="➡️ 뭐해, 머해, ㅁㅎ", inline=True)
    await ctx.send(embed=embed)

# 메롱하는 숭이
@bot.command(name="메롱")
async def merong(ctx):
    embed = discord.Embed(title="👅 메롱하는 숭이", description="", color=0x62c1cc)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1090085600201285654/1090280597982814298/IMG_9493.jpg")
    await ctx.send(embed=embed)

# 고백하는 숭이
@bot.command(aliases=['고백', '사귀자'])
async def love(ctx):
    embed = discord.Embed(title="😘 고백하는 숭이", description="", color=0x62c1cc)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1090085600201285654/1090281746425200710/IMG_9495.jpg")
    await ctx.send(embed=embed)

# 미안한 숭이
@bot.command(aliases=['미안', '미안해'])
async def sorry(ctx):
    embed = discord.Embed(title="🥹 미안한 숭이", description="", color=0x62c1cc)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1090085600201285654/1090283418991988806/20AFA056-5EBF-4E17-8214-2013A5205661.jpg")
    await ctx.send(embed=embed)

# 숭-하
@bot.command(aliases=['숭하', '하이', 'ㅎㅇ', '안녕'])
async def Hi(ctx):
    embed = discord.Embed(title="👋 숭-하", description="", color=0x62c1cc)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1090085600201285654/1090283490026717184/E06A7682-B72F-4CA5-BD8A-7755B2E54D37.png")
    await ctx.send(embed=embed)

# 숭이팅하는 숭이
@bot.command(aliases=['화이팅', 'ㅎㅇㅌ', '숭이팅'])
async def fighting(ctx):
    embed = discord.Embed(title="👏 숭이팅하는 숭이", description="", color=0x62c1cc)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1090085600201285654/1090283571140370472/C128E892-C98A-4286-8647-2137D7A59224.jpg")
    await ctx.send(embed=embed)

# 대답하는 숭이
@bot.command(aliases=['웅', 'ㅇㅇ', 'ㅇ'])
async def soong(ctx):
    embed = discord.Embed(title="👍 대답하는 숭이", description="", color=0x62c1cc)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1090085600201285654/1090283651251585045/B96A14C4-C981-4F34-8BE2-BA9AD69B4A6C.jpg")
    await ctx.send(embed=embed)

# 머하냐고 묻는 숭이
@bot.command(aliases=['뭐해', '머해', 'ㅁㅎ'])
async def WAYD(ctx):
    embed = discord.Embed(title="﹖ 머하냐고 묻는 숭이", description="", color=0x62c1cc)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1090085600201285654/1090283755605852281/F2B6BD9C-F831-4C5E-AEDF-0D68F26CD745.jpg")
    await ctx.send(embed=embed)





bot.run('Token')