#899641658805714964
#ODk5NjQxNjU4ODA1NzE0OTY0.YW1ulQ.cX69iQF9YWDBVVSHanfcaWmGjuY
# 899649487570599958
# 900355089561186345 id msg
from datetime import datetime
import discord
import re
import json
import time
from discord import client
from discord import member
from discord import channel
from discord.ext import commands
# from discord.flags import Intents
from discord.member import Member
from discord.utils import get
from googletrans import Translator

translator = Translator()

Intents = discord.Intents

intents = Intents.all()

# intents = Intents.all()
bot = discord.Client(intents=intents) #intents=intents
bot = commands.Bot(command_prefix='>>', intents=intents) #intents=intents
# intents = discord.Intents.all
# intents.members = True
@bot.command()
async def text(ctx, *, arg):
    await ctx.channel.send(arg)

@bot.command()
async def translate(ctx, lang, *, text):
    translator = Translator()
    display_translation = translator.translate(text, dest=lang).text
    embed = discord.Embed(color=discord.Color.dark_theme())
    embed.add_field(name=f"Language : {lang} ", value=f'{display_translation}')
    # await ctx.send(display_translation.text)
    await ctx.send(embed=embed)
    print("check")
    print(text)
    print(display_translation)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    # channel = discord.utils.get(ctx.guild.channels,name="join")
    # await channel.send(f"{member.mention} IRASSHAI !OwO!")

# @bot.command()
# async def send(ctx, channel, *, content):
#     channel = client.get_channel(int(channel))
#     await channel.send(content)

# @bot.event
# async def on_message(message):
#     print(message)
#     channel =  bot.get_channel(int('900798783372275723'))
#     if str(message.channel) == 'join' and str(message.type) == "MessageType.new_member":
#         embed = discord.Embed(title="สวัสดีไอหน้าโง่", description=message.author, color=0x13f2f2)
#         embed.set_author(name = message.author, icon_url = message.author.avatar_url)
#         embed.set_footer(icon_url = message.author.avatar_url, text = f"Requested by {message.author}")
#         await channel.send(embed = embed)
#         # message.author.avatar_url
@bot.event
async def on_member_join(member):
    channel =  bot.get_channel(int('900798783372275723'))
    embed = discord.Embed(title="สวัสดีไอหน้าโง่", description=member, color=0x13f2f2)
    embed.set_author(name = member, icon_url = member.avatar_url)
    embed.set_footer(icon_url = member.avatar_url, text = f"Requested by {member}")
    await channel.send(embed = embed)

@bot.event
async def on_member_remove(member):
    channel =  bot.get_channel(int('900798783372275723'))
    embed = discord.Embed(title="ลาก่อนไอหน้าโง่", description=member, color=0x13f2f2)
    embed.set_author(name = member, icon_url = member.avatar_url)
    embed.set_footer(icon_url = member.avatar_url, text = f"Requested by {member}")
    await channel.send(embed = embed)

@bot.event
async def on_raw_reaction_add(reaction):
    # ✅
    print(reaction)
    print(reaction.message_id)
    print(reaction.member)
    print(type(reaction.member.guild.roles))
    role = discord.utils.get(reaction.member.guild.roles, name="verify")
    role1 = discord.utils.get(reaction.member.guild.roles, name="verify1")
    role2 = discord.utils.get(reaction.member.guild.roles, name="verify2")
    role3 = discord.utils.get(reaction.member.guild.roles, name="verify3")
    role4 = discord.utils.get(reaction.member.guild.roles, name="verify4")
    channel = bot.get_channel(int('900355045076398112'))
    print(reaction.member.roles)
    print(role)
    print(reaction.emoji.name)
    if reaction.emoji.name == '✅' and reaction.message_id == 900355089561186345:
        if str(reaction.member.roles).count(str('900356642653220905')) >= 1:
            print("check")
        else:
            await reaction.member.add_roles(role)
            await channel.send(f'{reaction.member.mention} YOU HAS BEEN VERIFY' , delete_after = 10)
    elif reaction.emoji.name == '🐱' and reaction.message_id == 900355089561186345:
        if str(reaction.member.roles).count(str('900770196757819452')) >= 1:
            print("check")
        else:
            await reaction.member.add_roles(role1)
            await channel.send(f'{reaction.member.mention} YOU HAS BEEN VERIFY' , delete_after = 10)
    elif reaction.emoji.name == '🐶' and reaction.message_id == 900355089561186345:
        if str(reaction.member.roles).count(str('900770388089405541')) >= 1:
            print("check")
        else:
            await reaction.member.add_roles(role2)
            await channel.send(f'{reaction.member.mention} YOU HAS BEEN VERIFY' , delete_after = 10)
    elif reaction.emoji.name == '🐭' and reaction.message_id == 900355089561186345:
        if str(reaction.member.roles).count(str('900770382745837568')) >= 1:
            print("check")
        else:
            await reaction.member.add_roles(role3)
            await channel.send(f'{reaction.member.mention} YOU HAS BEEN VERIFY' , delete_after = 10)
    elif reaction.emoji.name == '🐰' and reaction.message_id == 900355089561186345:
        if str(reaction.member.roles).count(str('900770458159435796')) >= 1:
            print("check")
        else:
            await reaction.member.add_roles(role4)
            await channel.send(f'{reaction.member.mention} YOU HAS BEEN VERIFY' , delete_after = 10)


@bot.command()
async def alarm(ctx, alarm_time:str, *, reason:str):
    # time = datetime.now().timetuple()
    while True:
        check_time = datetime.now().strftime('%H:%M')
        nap = ((int(alarm_time[:2:]) - int(check_time[:2:]))*3600) + (((60-int(alarm_time[3::])) + int(check_time[3::]))*60)
        print(nap)
        if alarm_time == check_time:
            await ctx.send(f"{ctx.author.mention} it time to {reason}")
            print(check_time)
            break
        else:
            print("No")
            time.sleep(nap)

    
# 🐱 🐶 🐭 🐰
# @bot.event
# async def on_raw_reaction_remove(reaction):
#     print(reaction)
#     print(reaction.message_id)
#     print(reaction.user_id)
#     guild = await client.fetch_guild(reaction.guild_id)
#     member = get(guild.members, id=reaction.user_id)
#     print(member)
#     # role = discord.utils.get(reaction.member.guild.roles, name="verify")
#     # print(role)
#     # print(reaction.emoji.name)
#     # if reaction.emoji.name == '✅' and reaction.message_id == 900355089561186345:
#     #     print("check")
#     #     await reaction.member.remove_roles(role)
#     #     await reaction.member.send("YOU DELETED YOUR ROLE")
# @bot.event
# async def on_raw_reaction_remove(payload):

#     msgID = 754487460142121070  
#     user = payload.user_id
#     member = payload.member

#     guild_id = payload.guild_id
#     guild = discord.utils.find(lambda g : g.id == guild_id, member.guilds)
#     role = get(member.guild.roles, name="penis")

#     if payload is not None:
#         if payload.message_id == msgID:
#             if str(payload.emoji) == "<:bbc:639345897922101248>":
#                 await member.add_removes(role)


#bot = commands.Bot(command_prefix='?',help_command=None)
bot.run('ODk5NjQxNjU4ODA1NzE0OTY0.YW1ulQ.cX69iQF9YWDBVVSHanfcaWmGjuY')
