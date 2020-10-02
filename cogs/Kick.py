import discord
from discord.ext import commands
import os

class Kick(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		await member.kick(reason=reason)
		await ctx.send(f"{member.mention} Kicklendi\nSebep : {reason}")
		log = os.environ.get("LOG_ID")
		await log.send(f"{member} Kicklendi\nSebep : {reason}")

def setup(client):
	client.add_cog(Kick(client))
