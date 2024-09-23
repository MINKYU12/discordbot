import discord
import asyncio

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

spamming = False  # 도배 상태를 저장하는 변수
spam_task = None  # 도배 작업을 관리하는 변수
spam_message = "이것은 도배 메시지입니다!"  # 기본 도배 메시지

async def send_spam(channel):
    """지정된 채널에 메시지를 반복적으로 보냄"""
    while spamming:
        await channel.send(spam_message)
        await asyncio.sleep(1)  # 메시지 전송 간격(1초)

@client.event
async def on_ready():
    print(f'로그인됨: {client.user}')

@client.event
async def on_message(message):
    global spamming, spam_task, spam_message

    if message.author == client.user:
        return  # 봇이 스스로의 메시지에 반응하지 않게 함

    if message.content.startswith(";도배 "):  # 접두사 ;로 시작
        spam_message = message.content[4:]  # ';도배 ' 이후의 메시지를 저장
        if not spamming:
            spamming = True
            spam_task = asyncio.create_task(send_spam(message.channel))  # 도배 작업 시작
            await message.channel.send(f"도배를 '{spam_message}' 메시지로 시작합니다.")
        else:
            await message.channel.send("이미 도배가 진행 중입니다.")

    elif message.content == ";도배중지":
        if spamming:
            spamming = False
            spam_task.cancel()  # 도배 작업 중지
            await message.channel.send("도배를 중지합니다.")
        else:
            await message.channel.send("현재 도배가 진행 중이 아닙니다.")

client.run(MTI1NDM0NDY4NTI4Mzk3MTA4Mg.GVclWO.PLrXsW9XUJYFj2OPq2xivx9Ko4kKk8iIEMkXyc)
