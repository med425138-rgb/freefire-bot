import os
import discord
from discord import app_commands
from discord.ext import commands

# 1. Configuration
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 2. On Ready Event
@bot.event
async def on_ready():
    print(f'✅ L-Bot Online b smiyat: {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"❌ Error f Sync: {e}")

# 3. Slash Command 1 (/ping)
@bot.tree.command(name="ping", description="Test l-bot status")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong! L-bot khddam 24/7 mn Render Cloud!")

# 4. Slash Command 2 (/register)
@bot.tree.command(name="register", description="Register team f Scrim")
@app_commands.describe(team_name="Smiya d l-team", captain="Tag d l-capitaine")
async def register(interaction: discord.Interaction, team_name: str, captain: discord.Member):
    embed = discord.Embed(
        title="🔥 Free Fire Scrim Registration",
        description=f"L-team **{team_name}** t-sjjlat b success!",
        color=discord.Color.green()
    )
    embed.add_field(name="Capitaine", value=captain.mention, inline=True)
    embed.set_footer(text="Apostado Manager")
    await interaction.response.send_message(embed=embed)

# 5. Run l-Bot b Token mn Environment Variables
TOKEN = os.environ.get("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Token ma kaynsh f Environment Variables!")
