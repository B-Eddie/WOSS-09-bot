import discord
from discord.ext import commands
import os
from wossan import retrieve_announcements

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
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
async def on_member_join(member):
    guild = member.guild
    guild_id = 1225912243477024778  # Replace with the desired guild ID
    if guild.id == guild_id:
        channel_id = 1248103293406806077  # Replace with the desired channel ID
        channel = guild.get_channel(channel_id)
        if channel is not None:
            await channel.send(f"Welcome {member.mention} to the server! We're glad to have you here. Please follow the following steps in order to verify:")
            embed = discord.Embed(
                title="Instructions",
                description='''HDSB Registered Name:\nHDSB Email:\nVerification Keyword found in #rules:'''
            )
            await channel.send(embed=embed)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await tree.sync()

bot.run(os.getenv('TOKEN'))