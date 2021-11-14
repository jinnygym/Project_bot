import discord
from discord.utils import get
import youtube_dl
import asyncio
import itertools
# from googletrans import Translator

from AMusicPlayer import MusicPlayer
from AYTDLSource import YTDLSource
# translator = Translator()

youtube_dl.utils.bug_reports_message = lambda: ''  # การประกาศตัวเเปร


class Botmusicallplaylist:
    # classให้ 1-discordbot ดึงไปใช้งาน
    # ^
    # v
    # ใช้ในการประการclass __init__เป็น constructor(ตัวสร้าง) หรือก็คือ การใช้oopของpython เอาไว้ประกาศตัวใช้classให้ใช้ง่ายๆ
    # https://stackpython.medium.com/python-oop-ep-1-oop-%E0%B8%84%E0%B8%B7%E0%B8%AD%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3-f85ba48591f3
    def __init__(self):
        self.players = {}

    async def play(self, ctx, search: str):
        self.bot = ctx.bot  # ประกาดตัวเเปรทั้งclass
        self._guild = ctx.guild  # guild คือการที่เราใช้เซิฟนี้
        channel = ctx.author.voice.channel
        voice_client = get(self.bot.voice_clients, guild=ctx.guild)
# ถ้าbotยังไม่อยู่ในdis ก็จะเข้าifเเรกเพื่อเรียกbotเข้ามาในห้องเเล้วawait ctx.channel.send("Hi i'm here !!") หรือก็คือให้บอกพิมออกมาว่าhi i'm here
        if voice_client == None:
            await ctx.channel.send("Hi i'm here !!")
            await channel.connect()
            voice_client = get(self.bot.voice_clients, guild=ctx.guild)
# "บอทจะเเกล้งทำเป็นพิมเหมือนคนที่กำลังจะพิม 'https://media.discordapp.net/attachments/881275787582537880/907993684123983952/unknown.png'"
        await ctx.trigger_typing()

        _player = self.get_player(ctx)
        # source เป็นการล้างข้อมูลที่ถูกบันทึกไว้ใน ytdlทุกครั้งที่เล่นเพลงใหม่
        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)

        await _player.queue.put(source)

    players = {}
# 'เป็นcommandที่เหมือนกันกับ play เลยเเต่เปลียนเป็น play เป็น p'

    async def p(self, ctx, search: str):
        self.bot = ctx.bot
        self._guild = ctx.guild  # guild คือการที่เราใช้เซิฟนี้
        channel = ctx.author.voice.channel
        voice_client = get(self.bot.voice_clients, guild=ctx.guild)

        if voice_client == None:
            await ctx.channel.send("I'm here !")
            await channel.connect()
            voice_client = get(self.bot.voice_clients, guild=ctx.guild)

        await ctx.trigger_typing()

        _player = self.get_player(ctx)
        # source เป็นการล้างข้อมูลที่ถูกบันทึกไว้ใน ytdlทุกครั้งที่เล่นเพลงใหม่
        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)
        await _player.queue.put(source)

    players = {}
# อันนี้คือการเเก้errorทั้งหมด
# เป็นการที่บอกว่าคนที่สั่งคำสั่งอยู่ในห้องหรือเปล่า

    def get_player(self, ctx):
        # ถ้าฟังก์ชันไม่errorจะเข้าtry
        try:
            player = self.players[ctx.guild.id]
        # errorเข้าexcept
        except:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    async def stop(self, stopthemusic):
        # ประกาศตัวเเปร player
        player = self.get_player(stopthemusic)
        voice_client = get(self.bot.voice_clients, guild=stopthemusic.guild)
        if voice_client == None:
            # มีคนอยู่ในห้องมั้ยไม่ก็await เเละก็ลบข้อความหลังจากbotพิมข้อความเเล้ว10sec
            await stopthemusic.channel.send("Bot isn't connected to your room", delete_after=10)
            return
        if voice_client.channel != stopthemusic.author.voice.channel:  # ถ้าคนไม่อยู่ในห้องก็ไม่สามารถจะใช้ได้
            await stopthemusic.channel.send("Now bot isn't in your room he on .{0} room".format(voice_client.channel))
            return
        # ถ้าเราอยู่ให้ห้องสามารถstopได้เลยเเล้วยังลบqueueทั้งหมดให้อีกด้วย ด้วยคำสั่ง (player.queue = asyncio.Queue()เหมือนการทำให้ init เป็นค่าเริ่มต้น) เลยทำให้queueว่าง !!
        else:
            player.queue = asyncio.Queue()
            voice_client.stop()

    async def pause(self, bthemusic):
        voice_client = get(self.bot.voice_clients, guild=bthemusic.guild)
        if voice_client == None:  # มีคนอยู่ในห้องมั้ยไม่ก็await
            await bthemusic.channel.send("Bot isn't connected to your room", delete_after=10)
            return
        # ถ้าคนไม่อยู่ในห้องก็ไม่สามารถจะใช้ได้หรือไม่สามรถpauseเพลงได้นั้นเอง
        if voice_client.channel != bthemusic.author.voice.channel:
            await bthemusic.channel.send("Now bot isn't in your room he on {0} room".format(voice_client.channel))
            return
        # ถ้าคนที่สั่งbotอยู่ในห้องก็สามารถ pause เพลงได้
        else:
            voice_client.pause()

    async def resume(self, stillplaymusic):
        voice_client = get(self.bot.voice_clients, guild=stillplaymusic.guild)
        if voice_client == None:  # มีคนอยู่ในห้องมั้ยไม่ก็await
            await stillplaymusic.channel.send("Bot isn't connected to your room", delete_after=10)
            return
        # ถ้าคนไม่อยู่ในห้องก็ไม่สามารถจะใช้ได้หรือไม่สามารถเล่นเพลงต่อได้นั้นเอง
        if voice_client.channel != stillplaymusic.author.voice.channel:
            await stillplaymusic.channel.send("Now bot isn't in your room he on {0} room".format(voice_client.channel))
            return
        # ถ้าคนที่สั่งbotอยู่ในห้องก็สามารถ reseumeต่อเลย
        else:
            voice_client.resume()
# คำสั่งdis bot

    async def dis(self, ctx):
        voice_client = get(self.bot.voice_clients, guild=ctx.guild)
        # เป็นการเอาบอทออกจากdiscordโดยcommand [dis ถ้าคนอยู่ในห้องด้วย!!!!
        if voice_client.channel == ctx.author.voice.channel:
            del self.players[ctx.guild.id]
            await ctx.voice_client.disconnect()
        # ถ้าคนไม่อยู่ในห้องdiscord ห้องที่บอทอยู่เราก็ไม่สามารถเอาbot ออกจากห้องได้เเล้วจะsendออกมาเป็น what do you want??
        elif voice_client.channel != ctx.author.voice.channel:
            await ctx.channel.send("What do you want ??" + self.author.name)
# คำสั่งleavebot เป็นคำสั่งที่เหมือนกันdisบอทเลยเเต่เพิ่มcommadให้คนใช้งานได้ง่ายขึ้น

    async def leave(self, ctx):
        voice_client = get(self.bot.voice_clients, guild=ctx.guild)
        if voice_client.channel == ctx.author.voice.channel:
            del self.players[ctx.guild.id]
            await ctx.voice_client.disconnect()
         # ถ้าคนไม่อยู่ในห้องdiscord ห้องที่บอทอยู่เราก็ไม่สามารถเอาbot ออกจากห้องได้เเล้วจะsendออกมาเป็น what do you want??
        elif voice_client.channel != ctx.author.voice.channel:
            await ctx.channel.send("What do you want ??" + self.author.name)

    async def queue(self, queue):
        voice_client = get(self.bot.voice_clients, guild=queue.guild)
        # ถ้าไม่อยู่ในห้องที่บอทอยู่ก็ไม่สามารถดูqueneได้
        if voice_client == None or not voice_client.is_connected():
            await queue.channel.send("Bot isn't connected to your room", delete_after=10)
            return

        player = self.get_player(queue)
        # ถ้าเพลงไม่มีเเล้วในqueueหรือเพลงหมดเเล้วบอทจะพิมออกมาว่า No more queue to play the Music!!!
        if player.queue.empty():
            return await queue.send('No more queue to play the Music!!!', delete_after=10)
        # ถ้ามีเพลงอยู่queue มากกว่า0 ก็จะสามารถดูqueueได้
        upcoming = list(itertools.islice(
            player.queue._queue, 0, player.queue.qsize()))
        fmt = '\n'.join(f'**`{_["title"]}`**' for _ in upcoming)
        embed = discord.Embed(
            title=f'Have {len(upcoming)} music left.', description=fmt, color=0x61F2F2)
        await queue.send(embed=embed)

    async def q(self, queue):
        voice_client = get(self.bot.voice_clients, guild=queue.guild)
        # ถ้าไม่อยู่ในห้องที่บอทอยู่ก็ไม่สามารถดูqueneได้
        if voice_client == None or not voice_client.is_connected():
            await queue.channel.send("Bot isn't connected to your room", delete_after=10)
            return

        player = self.get_player(queue)
        if player.queue.empty():
            return await queue.send('No more queue to play the Music!!!', delete_after=10)

        upcoming = list(itertools.islice(
            player.queue._queue, 0, player.queue.qsize()))
        fmt = '\n'.join(f'**`{_["title"]}`**' for _ in upcoming)
        embed = discord.Embed(
            title=f'Have {len(upcoming)} music left.', description=fmt, color=0x61F2F2)
        await queue.send(embed=embed)

    async def playlist(self, queue):
        voice_client = get(self.bot.voice_clients, guild=queue.guild)

        if voice_client == None or not voice_client.is_connected():
            await queue.channel.send("Bot isn't connected to your room", delete_after=10)
            return

        player = self.get_player(queue)
        if player.queue.empty():
            return await queue.send('No more queue to play the Music!!!', delete_after=10)

        upcoming = list(itertools.islice(
            player.queue._queue, 0, player.queue.qsize()))
        fmt = '\n'.join(f'**`{_["title"]}`**' for _ in upcoming)
        embed = discord.Embed(
            title=f'Have {len(upcoming)} music left.', description=fmt, color=0x99F261)
        await queue.send(embed=embed)

    async def skip(self, skipMusic):
        voice_client = get(self.bot.voice_clients, guild=skipMusic.guild)
        # ถ้าคนไม่อยู่ในห้องก็ไม่สามารถใช้คำสั่งskipได้
        if voice_client.channel != skipMusic.author.voice.channel:
            await skipMusic.channel.send("Your aren't in that room !", delete_after=10)
        # คนอยู่ในห้องเท่านั้นที่สามารถใช้command skipได้
        else:
            # ถ้าไม่มีเพลงให้skip ก็จะไม่สามารถskipเพลงได้เเล้วเเล้วขึ้น sendว่า No more song to skip the Music!
            if not voice_client.is_playing():
                await skipMusic.channel.send("No more song to skip the Music!", delete_after=10)
                return
            # ถ้ามีเพลงให้skipก็ทำให้เพลงนั้นหยุดเเล้วขึ้นเพลงใหม่เลย พร้อมจะพูดออกมาว่า คนที่skipเพลงได้skippedเเล้ว
            voice_client.stop()
            await skipMusic.send(f'**`{skipMusic.author.name}`** Skipped the Music!!')

    async def s(self, skipMusic):
        voice_client = get(self.bot.voice_clients, guild=skipMusic.guild)
        if voice_client.channel != skipMusic.author.voice.channel:
            await skipMusic.channel.send("Your aren't in that room !", delete_after=10)

        else:
            if not voice_client.is_playing():
                await skipMusic.channel.send("No more song to skip the Music!", delete_after=10)
                return
            voice_client.stop()
            await skipMusic.send(f'**`{skipMusic.author.name}`** Skipped the Music!!')

    async def remove_(self, ctx, pos: int = None):
        vc = ctx.voice_client
        # ถ้า บอทไม่อยู่ในห้องก็ไม่สามารถส่งคำสั่งนี้ได้
        if not vc or not vc.is_connected():
            embed = discord.Embed(
                title="", description="Bot isn't connected to your room", color=discord.Color.green())
            return await ctx.send(embed=embed)
        player = self.get_player(ctx)
        if player.queue.empty():
            return await ctx.send('No more queue to play the Music!!!', delete_after=10)
        # ใส่ตำเเหน่งของqueueลงไปเเล้วจะลบเพลงนั้นออกจากqueue
        elif pos == None:
            player.queue._queue.pop()
            embed = discord.Embed(
                title="", description=f'remove song !!', color=discord.Color.green())
            await ctx.send(embed=embed)
        # ถ้าไม่ก็จะลบตำเเหน่งสุดท้ายของqueueออก
        else:
            try:
                s = player.queue._queue[pos-1]
                del player.queue._queue[pos-1]
                embed = discord.Embed(
                    title="", description=f"Removed [{s['title']}]({s['webpage_url']}) [{s['requester'].mention}]", color=discord.Color.green())
                await ctx.send(embed=embed)
                # ถ้าไม่มีเพลงที่จะลบก็ไม่สามารถลบเพลงนั้นออกมาได้
            except:
                embed = discord.Embed(
                    title="", description=f'Could not find a track for "{pos}"', color=discord.Color.green())
                await ctx.send(embed=embed)

    # async def loop(self ,ctx: commands.Context):
    #     if not ctx.voice_client.is_playing:
    #         return await ctx.send('Nothing being played at the moment.')
    #     ctx.voice_client_state.loop = not ctx.voice_client_state.loop
    #     await ctx.message.add_reaction('✅' , delete_after=20)
    # async def t(self, ctx, *, message):
    #     language = translator.detect(message)
    #     translation = translator.translate(message)
    #     embed = discord.Embed(color=discord.Color.dark_theme())
    #     embed.add_field(name=f"Language: {language} ", value=f'{translation}')
    #     await ctx.send(embed=embed)
