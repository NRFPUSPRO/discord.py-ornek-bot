import discord
from discord.ext import commands
from discord.utils import get


class OtoRol(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_member_join(self, member):
		rol = "Üye"
		role = get(member.guild.roles, name=rol)
		await member.add_roles(role)


def setup(client):
	client.add_cog(OtoRol(client))
