import discord
from discord.ext import commands
from cogwatch import Watcher
import os

client = commands.Bot(command_prefix="!")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Doing bot things"))
    watcher = Watcher(client, path='bot/cogs', debug=False)
    await watcher.start()
    print("Bot is ready.")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')



client.run(token)
