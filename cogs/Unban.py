import discord
from discord.ext import commands
import os
 
class Unban(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, userID):
		user = discord.Object(id=userID)
		await ctx.guild.unban(user)
        

		

def setup(client):
	client.add_cog(Unban(client))
