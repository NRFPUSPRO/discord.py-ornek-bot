import discord
from discord.ext import commands
import os

class Unban(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, *, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split("#")

		for ban_entry in banned_users:
			user = ban_entry.user

			if (user.name, user.desciminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f"{user.mention}'ın Banı Kaldırıldı")
				log = os.environ.get("LOG_ID")
				await log.send(f"{member} İçin Ban Kaldırıldı")
				await ctx.send(f"{member} İçin Ban Kaldırıldı")
				return


def setup(client):
	client.add_cog(Unban(client))
