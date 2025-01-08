import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # 사용자가 서버에 입장할 때 이벤트를 트리거하기 위해 필요한 설정

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_member_join(member):
    # 서버에 들어온 사용자에게 DM을 보냄
    try:
        dm_channel = await member.create_dm()  # DM 채널 생성
        await dm_channel.send(f"안녕하세요! {member.name} 님, 게임개발팀 발순이입니다! 지금 <#1180851672612884581> 으로 가셔서 이모지 클릭 부탁드립니다")
    except discord.errors.Forbidden:
        print(f"{member.name} 님에게 DM을 보낼 수 없습니다.")  # DM을 보내지 못할 경우 오류 메시지 출력

bot.run('YOUR_BOT_TOKEN')  # 봇의 토큰으로 바꿔주세요
