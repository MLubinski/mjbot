import discord, os, asyncio
from discord.ext import commands
from typing import Optional
import datetime

class Onward(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.last_message = ""
        self.open_lobby = False
        self.lfg_channel = 850366126528397322
        self.report_channel = 850448818548899881
        self.mj_lfg_channel = 799871582897438750
        self.mj_report_channel = 827259886681194556
        self.mj_community_support_id = 851556193809727488
        self.emoji = '\N{THUMBS UP SIGN}'

    #Create an Onward PVP/PVE lobby for reactions.
    @commands.command(name="onward", type=["PVP","PVE"], host="", help="Posts an Onward LFG post.\n Usage:**'!onward PVP/PVE'**")
    @commands.cooldown(rate=1, per=3)
    async def onward(self, ctx, *type):

        if self.open_lobby:
            await ctx.message.delete()
            await ctx.message.author.send("There is already another lobby open. Go join that one.")
            #self.last_message
        else:
            host = ctx.author.name
            type = ' '.join(type)
            ctx.channel = self.client.get_channel(self.mj_lfg_channel)
            #onward_role = discord.utils.get(ctx.guild.roles)
            embed=discord.Embed(title=f"{host} is hosting an Onward {type} lobby.", description=f"React to this message to receive your points for the monthly leaderboard.")
            embed.add_field(name='Host', value=host, inline=True)
            embed.add_field(name='Type', value=type, inline=True)
            embed.set_thumbnail(url='https://i.imgur.com/cAJixfU.png')
            msg = await ctx.send(embed=embed)
            await msg.add_reaction(self.emoji)
            await asyncio.sleep(1)
            await ctx.message.delete()
            self.last_message = msg
            self.open_lobby = True
            #print(f"Last message is {message.id}. The lobby is {self.open_lobby}")

    #Ends the Onward PVP/PVE lobby that was previously opened.
    @commands.command(name="end", help="This command will end the open lobby and make room for another one.\n Usage: **!end**", pass_context = True)
    async def end(self, ctx):
        users = set()
        author = ctx.author.name
        time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        community_role = discord.utils.get(ctx.guild.roles, id=self.mj_community_support_id)
        #print(f"The start. Last message is {self.last_message}.")
        channel = self.client.get_channel(self.last_message.channel.id)
        message = await channel.fetch_message(self.last_message.id)
        for each in message.reactions:
            async for user in each.users():
                if user.bot == False:
                    users.add(user)

        if len(users) > 0:
            description = f"Thanks for playing **{', '.join(str(f'<@!{user.id}>') for user in users)}**!"
        else:
            description = f"No one joined this lobby { author }. You better find new friends."
        embed = discord.Embed(title=f"Recent Lobby Report <@!{community_role}>", description=description)
        embed.set_footer(text=f"Lobby closed at {time}")
        ctx.channel = self.client.get_channel(self.mj_report_channel)
        reaction_counter = await ctx.send(embed=embed)
        await self.last_message.delete()
        await ctx.message.delete()
        #await asyncio.sleep(1)
        #await reaction_counter.delete()

        self.open_lobby = False

#def get_channel(ctx, name=None):
#    for channel in ctx.guild.channels:
#        if channel.name == name:
#            return channel.id

def setup(client):
    client.add_cog(Onward(client))
