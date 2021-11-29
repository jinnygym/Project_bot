import discord
import youtube_dl
import asyncio
from functools import partial

# translator = Translator()

youtube_dl.utils.bug_reports_message = lambda: ''  # การประกาศตัวเเปร

# "ytdl_format_options เป็น confix จากyoutube ที่เราเอามาเพื่อจะเปิดเพลง"
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
# การดึงเสียงดึงvideo เเละก็ยังเป็นค่า default การดัดเเปลงเสียงต่างๆ
ffmpeg_options = {
    'options': '-vn',
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
}
# Discord เตรียมนำบอทเพลงมาใช้งานโดยจะเชื่อมต่อกับ YouTube โดยตรง
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

# classที่ให้ Aplaylistได้เอาไปใช้งาน


class YTDLSource(discord.PCMVolumeTransformer):
    # ใช้ในการประการclass __init__เป็น constructor(ตัวสร้าง) หรือก็คือ การใช้oopของpython เอาไว้ประกาศตัวใช้classให้ใช้ง่ายๆ
    # https://stackpython.medium.com/python-oop-ep-1-oop-%E0%B8%84%E0%B8%B7%E0%B8%AD%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3-f85ba48591f3
    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester
        self.title = data.get('title')
        self.web_url = data.get('webpage_url')

    def __getitem__(self, item: str):
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            data = data['entries'][0]

        await ctx.send(f'```ini\n[Added {data["title"]} to the Queue.]\n```')

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source, **ffmpeg_options), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        # "ใช้ในการเตรียมstreamเเทนการdowloading ถ้าlinkของyoutubeมันหมดเวลาเเชร์หรือลิงค์หมดอายุ"
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']
        to_run = partial(ytdl.extract_info,
                         url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url'], **ffmpeg_options), data=data, requester=requester)
