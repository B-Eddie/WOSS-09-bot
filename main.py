import discord
from discord.ext import commands
import os
from wossan import retrieve_announcements

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

tree = bot.tree

@tree.command(name="info", description="Provides information about the bot")
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="WOSS 09 bot",
        description="This is the custom bot made for the WOSS 09 discord server!",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

@tree.command(name="woss_announcements", description="Gets all the announcements from the WOSSAN website.")
async def woss_announcements(interaction: discord.Interaction):
    announcements = retrieve_announcements()
    await interaction.response.send_message(embed=announcements)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    for guild in bot.guilds:
        print(f'Bot added to server: {guild.name}')
        channel = guild.system_channel
        if channel is not None:
            await channel.send('Hey everyone! I\'m the WOSS 09 discord bot!')
    await tree.sync()

bot.run(os.getenv('TOKEN'))