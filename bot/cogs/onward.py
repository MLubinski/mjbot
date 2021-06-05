import discord
from discord.ext import commands

class Onward(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.last_message = ""

    #Create an Onward PVP/PVE Event for reacts
    @commands.command(name="onward", type=["PVP","PVE"], host="", help="Posts an Onward LFG post by typing '!onward PVP/PVE HOST'")
    async def onward(self, ctx, type, host):
        last_message = ""
        ctx.channel = self.client.get_channel(850366126528397322)
        message = await ctx.send(f"**{host} is hosting an Onward {type} lobby**\n React for points and join.")
        await ctx.message.delete()
        await message.add_reaction('\N{THUMBS UP SIGN}')
        self.last_message = message
        print(f"Last message is {message.id}.")

    @commands.command(name="end")
    async def end(self, ctx):
        #print(f"The start. Last message is {self.last_message.id}.")
        #msg = await ctx.channel.fetch_message(last_message.id)
        await self.last_message.delete()
        await ctx.message.delete()
        print(f"Deleted last message {self.last_message.id}.")

def setup(client):
    client.add_cog(Onward(client))
