import discord
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.mikeadmin = 103634856709230592

    @commands.has_role('Admin')
    @commands.cooldown(rate=1, per=60)
    @commands.command(name='channelsjodie', hidden=True)
    async def print_channels(self, ctx):
        if ctx.message.author.id == 103634856709230592:
            for guild in self.client.guilds:
                for channel in guild.text_channels:
                    await ctx.send(f"{channel.name} {channel.id}")
        else:
            pass

    #@commands.cooldown(rate=1, per=60)
    @commands.command(hidden=True)
    async def clearjodie(self, ctx, amount=2):
        if ctx.message.author.id == 103634856709230592:
            await ctx.channel.purge(limit=amount)
        else:
            pass

    @commands.command(pass_context=True, hidden=True)
    async def getguildjodie(self, ctx):
        if ctx.message.author.id == 103634856709230592:
            guild = ctx.message.guild.id
            await ctx.send(guild)
        else:
            pass

    @commands.command(pass_context=True, hidden=True)
    async def deletejodie(ctx, id):
        if ctx.message.author.id == 103634856709230592:
            await ctx.message.delete({id})
        else:
            pass

def setup(client):
    client.add_cog(Commands(client))
