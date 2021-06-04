import discord
from discord.ext import commands

class Onward(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Create an Onward PVP/PVE Event for reacts
    @commands.command(name="onward", type=["PVP","PVE"], host="", help="Posts an Onward LFG post by typing '!onward PVP/PVE HOST'")
    async def onward(self, ctx, type, host):
        ctx.channel = self.client.get_channel(796486608278519838)
        message = await ctx.send(f"**{host} is hosting an Onward {type} lobby**\n React for points and join.")
        await ctx.message.delete()
        await message.add_reaction('\N{THUMBS UP SIGN}')


def setup(client):
    client.add_cog(Onward(client))
