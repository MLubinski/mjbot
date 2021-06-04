import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Doing bot things"))
    print("I am online")

@client.command(name='channels')
async def print_channels(ctx):
    for guild in client.guilds:
        for channel in guild.text_channels:
            await ctx.send(f"{channel.name} {channel.id}")

@client.command()
async def clear(ctx, amount=100) :
    await ctx.channel.purge(limit=amount)

#!create [PvP/E event] [Host:] 0:00
@client.command(name="onward", type=["PVP","PVE"], host="", help="Sets up an Onward LFG post")
async def new_onward_lfg(ctx, type, host):
    ctx.channel = client.get_channel(850366126528397322)
    await ctx.send(f"{host} is starting an Onward {type} lobby. React for points and join.")


client.run(token)
