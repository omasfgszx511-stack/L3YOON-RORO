import os
import discord
from discord.ext import commands

# إعدادات الصلاحيات
intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

# حط آي دي الروم الصوتي هنا بين الأقواس
VOICE_CHANNEL_ID = 1425432496551759872  

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم: {bot.user}")
    
    # الاتصال بالروم أول ما يشتغل البوت
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel and isinstance(channel, discord.VoiceChannel):
        try:
            if not channel.guild.voice_client:
                await channel.connect(self_deaf=True)
                print(f"تم الانضمام بنجاح إلى الروم: {channel.name}")
        except Exception as e:
            print(f"حدث خطأ أثناء محاولة الاتصال: {e}")
    else:
        print("لم يتم العثور على الروم، تأكد من الآي دي (ID).")

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