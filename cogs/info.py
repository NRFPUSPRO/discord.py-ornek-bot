import discord
from discord.ext import commands

class Info(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["sinfo"])
    @commands.guild_only()
    async def server_info(self, ctx):
        for boost_basanlar in ctx.guild.premium_subscribers:
        	pass
        await ctx.send(f"Server'ın Adı : {ctx.guild.name}\nServer Sahibi : {ctx.guild.owner}\nServer'ın Açıklaması : {ctx.guild.description}\nBoost Sayısı : {ctx.guild.premium_subscription_count}\nBoost Basanlar = {boost_basanlar}\n")


def setup(client):
    client.add_cog(Info(client))