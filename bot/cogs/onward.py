import discord
from discord.ext import commands

class Onward(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.last_message = ""
        self.open_lobby = False

    #Create an Onward PVP/PVE lobby for reactions.
    @commands.command(name="onward", type=["PVP","PVE"], host="", help="Posts an Onward LFG post by typing '!onward PVP/PVE HOST'")
    async def onward(self, ctx, type, host):
        if self.open_lobby:
            await ctx.message.delete()
            await ctx.message.author.send("There is already another lobby open. Go join that one.")
        else:
            ctx.channel = self.client.get_channel(796486608278519838)
            message = await ctx.send(f"**{host} is hosting an Onward {type} lobby**\n React for points and join.")
            await ctx.message.delete()
            await message.add_reaction('\N{THUMBS UP SIGN}')
            self.last_message = message
            self.open_lobby = True
            #print(f"Last message is {message.id}. The lobby is {self.open_lobby}")

    #Ends the Onward PVP/PVE lobby that was previously opened.
    @commands.command(name="end")
    async def end(self, ctx):
        #print(f"The start. Last message is {self.last_message.id}.")
        await self.last_message.delete()
        await ctx.message.delete()
        #print(f"Deleted last message {self.last_message.id}. The lobby is {self.open_lobby}")
        self.open_lobby = False

def setup(client):
    client.add_cog(Onward(client))
