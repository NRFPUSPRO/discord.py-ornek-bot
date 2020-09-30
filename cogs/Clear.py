import discord
from discord.ext import commands


class Clear(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command(aliases=["purge"])
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount=5):
		await ctx.channel.purge(limit=amount+1)
		await ctx.send(f"{amount+1} Mesaj Silindi")
		#log = self.client.get_channel(760096837717065748)
		#await log.send(f"{amount+1} Mesaj Silindi")

def setup(client):
	client.add_cog(Clear(client))
