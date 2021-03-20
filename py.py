import discord
import asyncio

token = 'ODIyNjk4NjIwOTQzOTkwODE1.YFWDzA.Xve5QniKTcUnMuObQywHGE5DqQ0' #봇토큰
client = discord.Client()

@client.event
async def on_ready():
    print("봉준")
    while True:
        await client.change_presence(status=discord.Status.online,activity=discord.Game(f'{len(client.guilds)}개의 서버에 참가ㅣ.도움말'))
        await asyncio.sleep(4)


@client.event
async def on_message(message):
    if message.content.startswith('안녕') or message.content.startswith('환영해'):
        message = await message.channel.send(embed=discord.Embed(title='반가워 나는 `Tricker` 라고 해 잘부탁해! 도움말을 보고 싶다면 T도움말 을 입력해줘!', colour=discord.Colour.green()))  

client.run(token)
