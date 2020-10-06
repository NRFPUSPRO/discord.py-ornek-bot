import discord
from discord.ext import commands

class İstatistik(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=["sistatistik"])
    async def sunucuistatistik(self, ctx, guild: discord.Guild):
            await ctx.send(ctx.guild.name)
		
        
        
        
def setup(client):
    client.add_cog(İstatistik(client))