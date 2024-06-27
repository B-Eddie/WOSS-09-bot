import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

tree = bot.tree

@tree.command(name="info", description="Provides information about the bot")
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="WOSS 09 bot",
        description="This is the person bot of Murder of Codes!",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

@tree.command(name="woss_announcements", description="Gets all the announcements from the WOSSAN website.")
async def woss_announcements(interaction: discord.Interaction):
    translated_phrase = translate_phrase(phrase)
    await interaction.response.send_message(translated_phrase)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await tree.sync()  # Sync commands with Discord

bot.run(os.getenv('TOKEN'))