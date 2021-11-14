import discord
from discord.ext import commands
from Aplaylist import Botmusicallplaylist


Intents = discord.Intents

# intents = Intents.all()
# bot = discord.Client(intents=intents)  # intents=intents
# intents=intents
bot = commands.Bot(command_prefix='[', help_command=None)
# , intents=intents
# การใช้เรียกclass
allsongmethod = Botmusicallplaylist()

# "bot.event คือการที่เราไม่ต้องสั่งการอะไรเลยเเล้วบอทจะส่งค่ามาให้ตามที่เราเขียนไว้ตอนเเรกเฉยๆพอหลังจากนั้นก็เเค่เปิดบอทเเล้วการใช้งานฟังก์ชันนี้จะขึ้นให้อัตโนมัติ"
# เเต่ถ่้ามีif elif elseก็คือมันจะเหมือนbot.command


@bot.event
# "on ready คือเป็นค่าตอนที่เราเปิดบอทมาว่าเราต้องการให้รู้ว่าเราจะพิมว่าอะไรให้เรารู้ว่าบอทของเรามันออนไลน์เเล้วเพื่อนำไปใช่งานได้"
async def on_ready():
    print(f"{bot.user} going to onlinenow.")
    channel = bot.get_channel(int('907984563123400744'))
    await channel.send('ใช้งานผมอีกเเละเหนื่อย !!!')


@bot.event
# "เมื่อมีคนเข้ามา"
async def on_member_join(member):
    # "get channelเราจะเอาเลขห้องที่เราต้องการให้botตอบกลับไปเป็นembed หรือก็คือการบอก Welcome!! ของคำสั่งนี้นั้นเอง"
    channel = bot.get_channel(int('905131943237156954'))
    embed = discord.Embed(
        title="Welcome!!", description=member, color=0x13f2f2)
    embed.set_author(name=member, icon_url=member.avatar_url)
    embed.set_footer(icon_url=member.avatar_url, text=f"Requested by {member}")
    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    # "เมื่อมีคนออก(leave)" "ก็เเสดงembedออกมาเป็นการบอกว่าคนนี้ออกจากห้องเเล้วนะ!!!"
    channel = bot.get_channel(int('905131943237156954'))
    embed = discord.Embed(title="Good luck!!",
                          description=member, color=0x13f2f2)
    embed.set_author(name=member, icon_url=member.avatar_url)
    embed.set_footer(icon_url=member.avatar_url, text=f"Requested by {member}")
    await channel.send(embed=embed)


@bot.event
# "ถ้ามีข้อความที่เราตั้งขึ้นมาออย่างตัวอย่างข้างล่างก็คือ [user, [logout เเล้วมันจะออกค่าตามที่เราจะawaitออกไป >w<"
async def on_message(message):
    global message_lastseen, message2_lastseen
    if message.content == '[user':
        await message.channel.send(' Hello '+str(message.author.name)+" !!")
    elif message.content == '[logout':
        await bot.logout()
    await bot.process_commands(message)


# 'embed' = 'การจัดเเบ่งเป็นฝังๆเเล้วจัดให้เป็นรูปเเบบที่เราต้องการ'
@bot.command()
async def help(EMBED):
    # 'titleคือหัวสุดเป็นหัวข้อ descriptionคิอสิ่งที่เป็นหัวข้อย่อยจากหัวข้อหลัก' "https://cdn.discordapp.com/attachments/872769228351102976/907841379080740874/unknown.png"
    # 'colorเราจะสามารถเปลียนได้เเล้วค่าที่จะเปลียนคือ'  "https://media.discordapp.net/attachments/872769228351102976/907843134514417674/unknown.png"
    embed = discord.Embed(title="Help Command", url="https://dissabot.000webhostapp.com/",
                          description="Bot Command", color=0x9E4DD1)
    # embed.set_author(name = "test", icon_url=EMBED.author.avatar_url)หัว
    # 'thumbnail คือรูปที่เราจะมาเเปะไว้ฟังขวาของtitleที่มีช่องว่างเหลือ'
    # "https://media.discordapp.net/attachments/872769228351102976/907841614767095808/unknown.png"
    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/292678280824356864/896342974789742612/image0.jpg?width=415&height=415")
    # 'inline = True' 'คือการที่เราอยากเอาอีกค่าหรืออีกaddfieldมาอยู่ในบันทัดเดียวกัน'
    # 'inline = False' 'คือการที่เราอยากเว้นวรรคไปอีกบันทัด
    # '\n> คือการที่ให้มห้มันอยู่ในหัวข้อย่อไปอีกเหมือนการเว้นบรรทัดเเล้วจะมีembedเพิ่มขึ้นมา https://media.discordapp.net/attachments/907845009921933312/907873160597217310/unknown.png'
    embed.add_field(name="help", value="Get help command.", inline=False)
    embed.add_field(name="Play the Music",
                    value="\n> [play \n> [p", inline=True)
    embed.add_field(name="Stop the Music", value=" \n> [stop", inline=True)
    embed.add_field(name="Pause the Music", value=" \n> [pause", inline=False)
    embed.add_field(name="Skip the Music",
                    value="\n> [s \n> [skip", inline=True)
    embed.add_field(name="Resume the Music", value="\n> [resume", inline=True)
    embed.add_field(name="Music playlist",
                    value="\n> [queue \n> [playlist \n> [q", inline=False)
    embed.add_field(name="remove the Music",
                    value="\n> remove_ ", inline=True)
    embed.add_field(name="Disconnect Bot", value="\n> [dis", inline=True)
    embed.add_field(name="Say hi >,<", value="\n> [user", inline=False)
    # "setfooter คืออันที่อยู่ล่างสุดโดยคำสั่งนี้icon_urlคือการที่มันจะขึ้นเป็นวงกลมเล็กๆเเล้วก็อยู่ที่เราจะใส่อะไรลงไป"
    # 'ตัวอย่าง''https://media.discordapp.net/attachments/907845009921933312/907873985029623808/unknown.png'
    embed.set_footer(icon_url=EMBED.author.avatar_url,
                     text='type "[help" to use command')
    embed.set_image(
        url="https://media.discordapp.net/attachments/292678280824356864/896342974789742612/image0.jpg?width=415&height=415")
    # 'ตัวawait เป็นตัวที่จะทำให้บอทมันสั่งค่าออกมาในรูปเเบบembedที่เราจัดตั้งเอาไว้'
    # 'เช่น'
    # "ถ้าเราไม่ได้ใส่ awaitตัวนี้ลงไปค่าที่ได้จากการสั่งcommand'help'คือ https://media.discordapp.net/attachments/872769228351102976/907844348039802910/unknown.png"
    # "ถ้าเราใส่awaitไปค่าที่ได้จะเป็นเเบบนี้" 'https://media.discordapp.net/attachments/907845009921933312/907845026392981565/unknown.png?width=431&height=421'
    await EMBED.send(embed=embed)

# "การเรียกใช้commandจาก 'file.Aplaylist'โดยคำสั่งต่างๆที่เราสามารถใช้ได้ ใช้ข้างหลังdef"


@bot.command()
async def send(ctx):
    print(ctx.channel)
    await ctx.channel.send('Hello')


@bot.command()
async def play(ctx, *, search: str):
    await allsongmethod.play(ctx, search)


@bot.command()
async def p(ctx, *, search: str):
    await allsongmethod.play(ctx, search)


@bot.command()
async def stop(stopthemusic):
    await allsongmethod.stop(stopthemusic)


@bot.command()
async def pause(bthemusic):
    await allsongmethod.pause(bthemusic)


@bot.command()
async def resume(stillplaymusic):
    await allsongmethod.resume(stillplaymusic)


@bot.command()
async def dis(ctx):
    await allsongmethod.dis(ctx)


@bot.command()
async def leave(ctx):
    await allsongmethod.dis(ctx)


@bot.command()
async def queue(queue):
    await allsongmethod.queue(queue)


@bot.command()
async def q(queue):
    await allsongmethod.queue(queue)


@bot.command()
async def playlist(queue):
    await allsongmethod.playlist(queue)


@bot.command()
async def skip(skipMusic):
    await allsongmethod.skip(skipMusic)


@bot.command()
async def s(skipMusic):
    await allsongmethod.s(skipMusic)


@bot.command()
async def remove_(ctx, pos: int = None):
    await allsongmethod.remove_(ctx, pos)


@bot.command()
async def loop(ctx: commands.Context):
    await allsongmethod.loop(ctx)


# @bot.command()
# async def translate(ctx, lang, *, text):
#     list_lang = lang.split(',')
#     translator = Translator()
#     for item in list_lang:
#         display_translation = translator.translate(text, dest=item).text
#         embed = discord.Embed(color=discord.Color.dark_theme())
#         embed.add_field(
#             name=f"Language : {item} ", value=f'{display_translation}')
#         await ctx.send(embed=embed)


bot.run('ODk1NTU0ODMyNzI1ODU2MjY4.YV6Qbg.eLYJcwoFipIyM5OMtCuzwppZ8s0')
