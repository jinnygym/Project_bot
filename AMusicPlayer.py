import discord
import asyncio
from async_timeout import timeout
from AYTDLSource import YTDLSource

# เป็นclassให้ Aplaylist ให้สามารถใช้งานได้ง่ายขึ้น


class MusicPlayer:

    __slots__ = ('bot', '_guild', '_channel', '_cog',
                 'queue', 'next', 'current', 'np', 'volume')
    # ใช้ในการประการclass __init__เป็น constructor(ตัวสร้าง) หรือก็คือ การใช้oopของpython เอาไว้ประกาศตัวใช้classให้ใช้ง่ายๆ
    # https://stackpython.medium.com/python-oop-ep-1-oop-%E0%B8%84%E0%B8%B7%E0%B8%AD%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3-f85ba48591f3

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog
        self.queue = asyncio.Queue()
        self.next = asyncio.Event()
        self.np = None
        self.volume = .5
        self.current = None
        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        """main loop ของบอท"""
        # เมื่อบอทไม่ได้ทำงาน
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()
            # เมื่อbotไม่ได้error ให้บอทออกจากห้องdiscord หลังจากbotไม่ได้ทำอะไรเลยเป็นเวลา4นาที
            try:
                async with timeout(180):  # 4 นาที
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                return await self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as winza007:
                    await self._channel.send(f'There was an error processing your song.\n'
                                             f'```css\n[{winza007}]\n```')
                    continue
            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(
                source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            self.np = await self._channel.send(f'**Now Playing:** `{source.title}` requested by '
                                               f'`{source.requester}`')
            await self.next.wait()

            source.cleanup()
            self.current = None

            try:
                await self.np.delete()
            except discord.HTTPException:
                pass

    # async def destroy(self, guild):
    #     await self._guild.voice_client.disconnect()
    #     return self.bot.loop.create_task(self._cog.cleanup(guild))
