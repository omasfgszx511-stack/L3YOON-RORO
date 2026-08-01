import os
import discord

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = discord.Client(intents=intents)

# حط هنا آي دي الروم الصوتي الصحيح اللي تبيه يدخله
VOICE_CHANNEL_ID = 1425432496551759872  

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم: {bot.user}")
    
    # محاولة دخول الروم الصوتي تلقائياً فور تشغيل البوت
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel and isinstance(channel, discord.VoiceChannel):
        try:
            if not channel.guild.voice_client:
                await channel.connect(self_deaf=True)
                print(f"تم الانضمام بنجاح إلى الروم: {channel.name}")
        except Exception as e:
            print(f"خطأ أثناء محاولة دخول الروم: {e}")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
