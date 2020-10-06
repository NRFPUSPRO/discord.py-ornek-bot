import discord
from discord.ext import commands
import pyfiglet


class Ascii(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def ascii(self, ctx, metin, font=DEFAULT_FONT):
        await ctx.send(pyfiglet.figlet_format(metin, font=font))



def setup(client):
    client.add_cog(Ascii(client))