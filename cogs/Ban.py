import discord
from discord.ext import commands
import os

class Ban(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, *, reason="Belirtilmedi"):
		await member.ban(reason=reason)
		await ctx.send(f"{member.mention} Banlandı\nSebep : {reason}")
		log = self.client.get_channel(int(os.environ.get("LOG_ID")))
		await log.send(f"{member} Banlandı\nSebep : {reason}")


def setup(client):
	client.add_cog(Ban(client))
