import discord
from discord.ext import commands


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
				#log = self.client.get_channel(760096837717065748)
				await ctx.send(f"{member} İçin Ban Kaldırıldı")
				return


def setup(client):
	client.add_cog(Unban(client))
