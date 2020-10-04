import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from config import Token

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    channel = client.get_channel(665552690172002315)
    await channel.send("Test")

client.run(Token)