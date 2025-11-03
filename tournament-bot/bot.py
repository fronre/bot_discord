import discord
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True  # ضروري باش يقرا الرسائل
bot = commands.Bot(command_prefix="!", intents=intents)

players = []

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# 
@bot.command()
async def join(ctx):
    username = ctx.author.name
    if username in players:
        await ctx.send(f"⚠️ {username} راك مسجل من قبل!")
    else:
        players.append(username)
        await ctx.send(f"✅ {username} تم تسجيلك في البطولة!")

# عرض اللاعبين
@bot.command()
async def players_list(ctx):
    if not players:
        await ctx.send("📭 ما كاين حتى لاعب مسجل بعد.")
    else:
        message = "🏆 اللاعبين المسجلين:\n" + "\n".join(players)
        await ctx.send(message)

# أمر لتصفير القائمة (خاص بالإدمن فقط)
@bot.command()
@commands.has_permissions(administrator=True)
async def reset(ctx):
    global players
    players = []
    await ctx.send("♻️ تم تصفير قائمة اللاعبين!")

bot.run(TOKEN)
