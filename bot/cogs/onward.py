import discord, os, asyncio
from discord.ext import commands
from typing import Optional

class Onward(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.last_message = ""
        self.open_lobby = False
        self.channel = 796486608278519838
        self.emoji = '\N{THUMBS UP SIGN}'

    #Create an Onward PVP/PVE lobby for reactions.
    @commands.command(name="onward", type=["PVP","PVE"], host="", help="Posts an Onward LFG post by typing '!onward PVP/PVE HOST'")
    #@commands.cooldown(rate=1, per=5)
    async def onward(self, ctx, *type):
        if self.open_lobby:
            await ctx.message.delete()
            await ctx.message.author.send("There is already another lobby open. Go join that one.")
            self.last_message
        else:
            host = ctx.author.name
            ctx.channel = self.client.get_channel(self.channel)
            #message = await ctx.send(f"**{host} is hosting an Onward {type} lobby**\n React for points and join.")
            embed=discord.Embed(title=f"{host} is hosting an Onward {type} lobby.", description=f"React to this message to receive your points for the monthly leaderboard.")
            embed.add_field(name='Host', value=host, inline=True)
            embed.add_field(name='Type', value=type, inline=True)
            embed.set_thumbnail(url='https://i.imgur.com/cAJixfU.png')
            msg = await ctx.send(embed=embed)
            await ctx.message.delete()
            await msg.add_reaction(self.emoji)
            self.last_message = msg
            self.open_lobby = True
            #print(f"Last message is {message.id}. The lobby is {self.open_lobby}")

    #Ends the Onward PVP/PVE lobby that was previously opened.
    @commands.command(name="end", help="This command will end the open lobby and make room for another one.\n **!end**", pass_context = True)
    async def end(self, ctx):
        users = set()
        author = ctx.author.name
        #print(f"The start. Last message is {self.last_message}.")
        channel = self.client.get_channel(self.last_message.channel.id)
        message = await channel.fetch_message(self.last_message.id)
        for each in message.reactions:
            async for user in each.users():
                if user.bot == False:
                    users.add(user)

        if len(users) > 0:
            description = f"Thanks for playing **@{', '.join(str(user.name) for user in users)}**!"
        else:
            description = f"No one joined this lobby { author }. You better find new friends."

        embed = discord.Embed(title="Recent Lobby Report", description=description)
        reaction_counter = await ctx.send(embed=embed)
        await self.last_message.delete()
        await ctx.message.delete()
        await asyncio.sleep(5)
        await reaction_counter.delete()

        self.open_lobby = False


def setup(client):
    client.add_cog(Onward(client))
