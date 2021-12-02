import discord
from discord.ext import commands
from dotenv import dotenv_values
from config import *
bot = commands.Bot(command_prefix=PREFIX, help_command=None, description="Test Bot for The discord.py")

@bot.event
async def on_ready():
    print(f"{bot.user} going to online now.")

reactions = ['👍', '👎', '🐬', '🐷', '🐠']
@bot.command()
async def poll(ctx, message, *options: str):
    if message == None:
        await ctx.send('Please enter a message')
    if len(options) <= 1:
        await ctx.send('You need more than one option to vote!') 
    pollEmbed = discord.Embed(title=message, description="React with corresponding emoji to vote", color=0x7146CC)
    pollEmbed.set_footer(text='Poll created by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    pollEmbed.timestamp = ctx.message.created_at
    field = ""
    count = [1 for _ in range(len(options))]
    for x in range(len(options)):
        field += "{} {}\n\n".format(reactions[x], options[x])
    pollEmbed.add_field(name=field, value="\u200b", inline=False)
    for x in range(len(options)):
        text = "{} {}".format(reactions[x] ,count[x])
        pollEmbed.add_field(name=text, value="\u200b", inline=False)
    pollMsg = await ctx.send(embed=pollEmbed)
    for x in range(len(options)):
        await pollMsg.add_reaction(reactions[x])

async def updateEmbed(message,emoji):
    if message.embeds:
        if message.embeds[0].title:
            await message.edit(embed=message.embeds[0].set_field_at(reactions.index(emoji) + 1, name="{} {}".format(reactions[reactions.index(emoji)],message.reactions[reactions.index(emoji)].count) , value="\u200b", inline=False))

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.author == user:
        return
    try:
        await updateEmbed(reaction.message,reaction.emoji)
    except:
        pass

@bot.event
async def on_raw_reaction_remove(payload):
    message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
    try:
        await updateEmbed(message,payload.emoji.name)
    except:
        pass


bot.run("OTA3NTc0NTI5Mjg1NTc4NzYz.YYpKpQ.0cxOTTGNerq29VkZd_COF07QHwg")