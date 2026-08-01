import os
import discord
from discord.ext import commands

# إعدادات الصلاحيات
intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True
intents.message_content = True  # مهم لقراءة الأوامر في الشات

bot = commands.Bot(command_prefix="!", intents=intents)

# آي دي الروم الصوتي الاحتياطي (لو تبيه يدخل تلقائي أول ما يشتغل)
VOICE_CHANNEL_ID = 1425432496551759872  

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم: {bot.user}")

# أمر join لدخول الروم الصوتي الموجود فيه الشخص
@bot.command(name="join")
async def join_channel(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        if ctx.guild.voice_client:
            await ctx.guild.voice_client.move_to(channel)
        else:
            await channel.connect(self_deaf=True)
        await ctx.send(f"تم الانضمام إلى الروم الصوتي: **{channel.name}** ✅")
    else:
        await ctx.send("عليك الدخول إلى روم صوتي أولاً لكي أتمكن من الانضمام إليك! ❌")

@bot.event
async def on_voice_state_update(member, before, after):
    # إذا طلع البوت لأي سبب، يرجع يدخل تلقائياً
    if member.id == bot.user.id:
        if after.channel is None and before.channel is not None:
            print("تم إخراج البوت، جاري إعادة الاتصال...")
            channel = bot.get_channel(VOICE_CHANNEL_ID)
            if channel:
                try:
                    await channel.connect(self_deaf=True)
                    print("تمت العودة إلى الروم بنجاح.")
                except Exception as e:
                    print(f"فشل إعادة الاتصال: {e}")

# قراءة التوكن من إعدادات الموقع لحمايته
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
