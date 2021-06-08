import discord
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_role('Admin')
    @commands.cooldown(rate=1, per=60)
    @commands.command(name='channels', hidden=True)
    async def print_channels(self, ctx):
        for guild in self.client.guilds:
            for channel in guild.text_channels:
                await ctx.send(f"{channel.name} {channel.id}")

    @commands.has_role('Admin')
    @commands.cooldown(rate=1, per=60)
    @commands.command(hidden=True)
    async def clear(self, ctx, amount=1) :
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Commands(client))
