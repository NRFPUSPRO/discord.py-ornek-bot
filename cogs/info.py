import discord
from discord.ext import commands

class Info(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["sinfo"])
    @commands.guild_only()
    async def server_info(self, ctx):
        await ctx.send(f"Sunucu Adı : {ctx.guild.name}\nSunucu Açıklaması : {ctx.guild.description}\nSunucu Sahibi : {ctx.guild.owner}\nBoost Sayısı : {ctx.guild.premium_subscription_count}\nBoost Basan Kişiler : {"0" if ctx.guild.premium_subscribers = [] else ctx.guild.premium_subscribers}\nÜye Sayısı : {ctx.guild.member_count}")



def setup(client):
    client.add_cog(Info(client))
