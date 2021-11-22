import discord
import json
from Ejudge import ejudgeclass

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# @client.event
# async def on_ready(ctx, par):
#     await ctx.channel.send(f"Message +>  {par}, {ctx}")

@client.event
async def on_message(message):
    global message_lastseen, message2_lastseen
    if message.content.count("!chotipat entercoruse") >= 1:
        few = message.content.split()
        ejudgeclass.entercourse()         
        await message.channel.send('```สำเร็จ```')
    if message.content.count("!chotipat findejudge") >= 1:
        few = message.content.split()
        if len(few) == 2:
            await message.channel.send('```กรุณาใส่ข้อมูลก่อนทำรายการ```')
        else:
            datauser = ejudgeclass.findejudge(few[2])
            await message.channel.send('```Status => กำลังค้นหาชื่อ```')
            if datauser['status'] == 'success':
                embed=discord.Embed(title=message.author, description="#%s" %(datauser['data']['studentid']), color=0x826868)
                embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/Bd0au_i6rLJFx2rEo-Qnvu52PhDdD53AOSquCLujYzJMQYo4-0zsr6NVGL175iGEBr7BqO4mkXPJkJZTvQjSzCOsRbapX8ye=s0-d")
                embed.set_footer(text="กำลังค้นหาข้อมูลใน Ejudge")
                await message.channel.send(embed=embed)
                datauser = ejudgeclass.golink(datauser['data']['profile'], 27)

                listfew = []
                search = open("problem.txt","r", encoding="utf8")
                for line in search.readlines():
                    listfew.append(json.loads(line.strip()))
                listfewf = []
                for i in listfew:
                    if i['course'] == "Problem Solving in Information Technology 2021 (IT)":
                        boolvczxvczx = False
                        for j in datauser:
                            if j["problem"] == i['problem']:
                                boolvczxvczx = True
                                break
                        if boolvczxvczx == False:
                            listfewf.append(i)
                fdasfsda = []
                fdasfsda.append("เหลือข้อที่ยังไม่ได้ทำอยู่: " + str(len(listfewf)) + " ข้อ")
                for i in listfewf:
                    fdasfsda.append(str(i["problem"] + " | " + str(i["star"]) + " ดาว"))

                embed = discord.Embed(title="Ejudge Search", description='\n'.join(str(e) for e in fdasfsda), color=0x13f2f2)
                embed.set_author(name = 'Welcome back homie.', icon_url = 'https://cdn.discordapp.com/emojis/786631852931940382.gif?size=64')
                embed.set_footer(icon_url = message.author.avatar_url, text = f"Requested by {message.author}")
                await message.channel.send(embed = embed)
    if message.content == '!chotipat help':
        embed = discord.Embed(title=message.author, url="https://realdrewdata.medium.com/", set_author="", description="few", color=0x112244)
        await message.channel.send(embed = embed)
        await message.channel.send('```พิมคำว่า : สวัสดีครับอาจารย์โช \nเพื่อให้อาจารย์โชตอบกลับ```')
client.run('ODk1Mjk0NzU0NjM0NDY5Mzg3.YV2eNw.zB0SEomfc-X5qwyEWzVahQuR1W0')


