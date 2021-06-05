import discord
from discord.ext import commands
from cogwatch import Watcher
import os

client = commands.Bot(command_prefix="!")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Doing bot things"))
    watcher = Watcher(client, path='bot/cogs', debug=False)
    await watcher.start()
    print("Bot is ready.")

@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command(hidden=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('bot/cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
  else:
    print(f'Unable to load {filename[:-3]}')

def save_message(message):
    file = open('messages.txt')
    file.write(message.content + '\n')
    file.close()

client.run(token)
