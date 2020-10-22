import discord
from discord.ext import commands

class İstatistik(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=["sistatistik"])
    async def sunucuistatistik(self, ctx, guild: discord.Guild):
            await ctx.send(f"Sunucu Adı : {ctx.guild.name}\nSunucu Açıklaması : {ctx.guild.description}\nSunucu Sahibi : {ctx.guild.owner}\nBoost Sayısı : {ctx.guild.premium_subscription_count}\nBoost Basan Kişiler : {ctx.guild.premium_subscribers}\nÜye Sayısı : {ctx.guild.member_count}")
			
        
        
        
def setup(client):
    client.add_cog(İstatistik(client))