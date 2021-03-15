import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('채팅방 청소')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!클린'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='[ Delete Massage ]' + str(amount) + '개의 메시지가 삭제되었습니다', colour=discord.Colour.green()))
                await asyncio.sleep(2)
                await message.delete()
            else:
                await message.channel.send('```명령어 사용권한이 없습니다.```')
        except:
            pass

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
