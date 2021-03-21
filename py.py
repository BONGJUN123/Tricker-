import discord
import asyncio
import datetime
import time
from itertools import cycle

token = '봇 토큰' #봇토큰
channel = 인증채널 id 
veri_id = 인증역할 id
notice_id = 공지채널 id
come_id = 입장로그채널 id
exit_id = 퇴장로그채널 id

status = cycle(['T도움말', '개발자ㅣ봉준'])

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    await client.get_channel(come_id).send(f"{member.mention}님! 저희 봉준이네에 오신걸 환영합니다!")
    await client.get_channel(come_id).send(member.avatar_url)

@client.event
async def on_member_remove(member):
    await client.get_channel(exit_id).send(f"{member.mention}님! 저희 봉준이네에 다시 돌아오실꺼죠??")

@client.event
async def on_ready():
    print("봉준")

@client.event
async def on_message(message):
    if message.content.startswith('안녕') or message.content.startswith('환영해'):
        message = await message.channel.send(embed=discord.Embed(title='반가워 나는 `Tricker` 라고 해 잘부탁해! 도움말을 보고 싶다면 T도움말 을 입력해줘!', colour=discord.Colour.green())) 

    if message.content.startswith('T도움말') or message.content.startswith('T명령어'):
        embed = discord.Embed(colour=discord.Colour.red(), title='```Tricker 봇 도움말 입니다 ```')
        embed.add_field(name='안녕/환영해', value='안녕/환영해 라고 입력하면 봇이 자신의 소개를 합니다!', inline=True)
        embed.add_field(name='T밴/T킥', value='킥/밴 뒤에 멘션한 유저를 킥/밴을 합니다', inline=True)
        embed.add_field(name='T채널삭제/T폭파', value='이 명령어를 사용한 채널을 삭제합니다', inline=True)
        embed.add_field(name='T인증', value='지정된 채널에서 이 명령어를 실행하면 자동으로 인증권한이 들어갑니다', inline=True)
        embed.add_field(name='T공지', value='T공지 후 뒤에 작성한 말을 공지채널에 자동으로 전송해줍니다', inline=True)
        embed.add_field(name='T내놔', value='봇 오픈소스를 드립니다', inline=True)
        embed.add_field(name='T내정보', value='자신의 정보를 알려줍니다', inline=True)
        embed.add_field(name='T에펙', value='에프터 이펙트 CC2020의 링크를 보내줍니다', inline=True)
        embed.add_field(name='T미디어', value='미디어 인코더 CC2020의 링크를 보내줍니다', inline=True)
        embed.add_field(name='T전송', value='멘션한 유저에게 메시지를 보냅니다', inline=True)
        embed.set_footer(text='개발자ㅣ봉준')
        await message.channel.send(embed=embed)

    if message.content.startswith('T밴'):
        if message.author.guild_permissions.ban_members:
            try:
                target = message.mentions[0]
            except:
                await message.channel.send('유저가 지정되지 않았습니다')
                return
            
            j = message.content.split(" ")
            try:
                reason = j[2]
            except IndexError:
                reason = 'None'

            

            embed = discord.Embed(title='차단', description=f'🚫**{message.guild.name}**에서 차단되었습니다.\n사유: {reason}🚫', colour=discord.Colour.red())
            try:
                await target.send(embed=embed)
            except:
                pass
            await target.ban(reason=reason)

            embed = discord.Embed(title='✅  차단 성공', description=f'🚫**{target}**이 차단되었습니다.\n사유: {reason}🚫', colour=discord.Colour.green())
            await message.channel.send(embed=embed)

    if message.content.startswith('T킥'):
        if message.author.guild_permissions.ban_members:
            await message.delete()
            try:
                target = message.mentions[0]
            except:
                await message.channel.send('유저가 지정되지 않았습니다')
                return
            
            j = message.content.split(" ")
            try:
                reason = j[2]
            except IndexError:
                reason = 'None'

            

            embed = discord.Embed(title='추방', description=f'🚫**{message.guild.name}**에서 추방되었습니다.\n사유: {reason}🚫', colour=discord.Colour.red())
            try:
                await target.send(embed=embed)
            except:
                pass
            await target.kick(reason=reason)

            embed = discord.Embed(title='✅  추방 성공', description=f'🚫**{target}**이 추방되었습니다.\n사유: {reason}🚫', colour=discord.Colour.green())
            await message.channel.send(embed=embed)

    if message.content.startswith("T인증"): 
        if not message.channel.id == int(channel):
            return
        a = "T인증"

        def check(message):
            return message.author == message.author and message.channel == message.channel

        if message.content == a:
            role = discord.utils.get(message.guild.roles, id=veri_id)
            await message.channel.purge(limit=4)
            tjdrhdEmbed = discord.Embed(title='인증성공', color=0x04FF00)
            tjdrhdEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tjdrhdEmbed.add_field(name='1초후 인증역할이 부여됩니다.', value='** **', inline=False)
            tjdrhdEmbed.set_thumbnail(url=message.author.avatar_url)
            tjdrhdEmbed.set_footer(text='개발자ㅣ봉준')
            await message.channel.send(embed=tjdrhdEmbed)
            time.sleep(1)
            await message.author.add_roles(role)

    if message.content.startswith('T청소') or message.content.startswith('T삭제'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개 삭제됨', colour=discord.Colour.green()))
                await asyncio.sleep(2)
                await message.delete()
            else:
                await message.channel.send(f'{message.author.mention}')
                await message.delete()
                message = await message.channel.send(embed=discord.Embed(title='⚠️ `명령어 사용권한이 없습니다` ⚠️', colour=discord.Colour.red())) 
        except:
            pass 

    if message.content.startswith('T공지'):
        try:
            if message.author.guild_permissions.manage_messages:
                msg = message.content[4:]
                await message.delete()
                message = await message.channel.send(embed=discord.Embed(title='✔️ `공지가 제대로 등록되었습니다` ✔️', colour=discord.Colour.blue())) 
                embed = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
                embed.add_field(name="공지사항 안내 ", value=msg , inline=False)
                embed.set_footer(text='개발자ㅣ봉준')
                await client.get_channel(notice_id).send('@everyone', embed=embed)
            else:
                await message.channel.send(f'{message.author.mention}')
                await message.delete()
                message = await message.channel.send(embed=discord.Embed(title='⚠️ `명령어 사용권한이 없습니다` ⚠️', colour=discord.Colour.red())) 
        except:
            pass

    if message.content.startswith('T폭파') or message.content.startswith('T채널삭제'):
        try:
            if message.author.guild_permissions.ban_members:
                await message.channel.delete()
            else:
                await message.channel.send(f'{message.author.mention}')
                await message.delete()
                message = await message.channel.send(embed=discord.Embed(title='⚠️ `명령어 사용권한이 없습니다` ⚠️', colour=discord.Colour.red()))
        except:
            pass

    if message.content.startswith('T봇소스') or message.content.startswith('T내놔'):
        covidembed = discord.Embed(title='봇 소스를 받으려면 이곳을 누르세요', description="", color=0xFF0F13, url='https://github.com/BONGJUN123/Tricker-')
        covidembed.set_footer(text='개발자ㅣ봉준')
        await message.channel.send(embed=covidembed)

    if message.content.startswith("T내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="`이름`", value=message.author.name, inline=True)
        embed.add_field(name="`별명`", value=message.author.display_name, inline=False)
        embed.add_field(name="`가입일`", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="`아이디`", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text='개발자ㅣ봉준')
        await message.channel.send('', embed=embed)

    if message.content.startswith('T에펙'):
        jkembed = discord.Embed(title='ADOBE AFTER EFFECT', description="", color=0xFF0F13, url='https://mega.nz/file/pcgB2CDI#nxS2Jqy0BUfYAdIViVy3dfyoNN7EWJDB_WT6AUZFp_I')
        await message.channel.send(embed=jkembed)

    if message.content.startswith('T미디어'):
        jkembed = discord.Embed(title='ADOBE MEDIA EMCODER', description="", color=0xFF0F13, url='https://mega.nz/file/1BI3hKJD#riomLZQpv_BPBs9Pq8DQTI8zL-WCx8gZMaHNa4nohfU')
        await message.channel.send(embed=jkembed)

    if message.content.startswith('T전송'):
        await message.delete()
        if message.author.guild_permissions.manage_messages:
            msg = message.content[26:]
            await message.mentions[0].send(embed=discord.Embed(title=f"**{message.author.name}** 님이 전송하신 메시지: {msg}", colour=discord.Colour.blurple()))
            await message.channel.send(embed=discord.Embed(title=f'`{message.mentions[0]}`에게 DM을 보냈습니다', colour=discord.Colour.blue()))
            
        else:
            await message.channel.send(f'{member.mention}')
            message = await message.channel.send(embed=discord.Embed(title='⚠️ `명령어 사용권한이 없습니다` ⚠️', colour=discord.Colour.red()))
            return


client.run(token)
