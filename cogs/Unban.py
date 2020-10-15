import discord
from discord.ext import commands
import os

from discord.ext.commands.core import command
 
class Unban(commands.Cog):

	def __init__(self, client):
		self.client = client

	#@commands.command() Karışık Yöntem
	#@commands.guild_only()
	#@commands.has_permissions(ban_members=True)
	#async def unban(self, ctx, userID):
	#	user = discord.Object(id=userID)
	#	await ctx.guild.unban(user)
        
	@commands.command()  #Basit Yöntem
	@commands.guild_only()
	@commands.has_permissions(ban_members=True)	
	async def unban(self, ctx, member: str = ""):
		if member == "":
			await ctx.send("Lütfen Bir Kullanıcı Adı Girin")
			return
		membername, memberdiscriminator = member.split("#")
		banlar = await ctx.guild.bans()
		for b in banlar:
			if (b.user.name, b.user.discriminator) in (member, memberdiscriminator):
				await ctx.guild.unban(b.user)
				await ctx.send(f"{b.user}'ın Banı Kaldırıldı")
				return
			else:
				await ctx.send("Bu Kullanıcı Banlı Değil")
				return

def setup(client):
	client.add_cog(Unban(client))
