import discord
from discord.ext import commands

# استبدل التوكن هنا 🔒
TOKEN = "YOUR_BOT_TOKEN"

# تعريف البوت
intents = discord.Intents.default()
intents.message_content = True  # ضروري باش يقرا الرسائل
bot = commands.Bot(command_prefix="!", intents=intents)

