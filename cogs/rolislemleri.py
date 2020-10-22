import discord
from discord.ext import commands

class Rol(commands.Cog):
	def __init__(self, client):
		self.client = client
		

	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(manage_roles=True)
	async def rol_ekle(self, ctx, member: discord.Member, *, rol):
		try:
			await member.add_roles(rol)
			await ctx.send(f"{rol} Rolü Eklendi")
			rapor_kanali = self.client.get_channel(int(os.environ.get("LOG_ID")))
		    await rapor_kanali.send(f"{member} Kişisine {rol} Rolü Eklendi")
		except:
			await ctx.send("Böyle Bir Rol Yok")



	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(manage_roles=True)
	async def rol_kaldır(self, ctx, member:discord.Member, *, rol):
		try:
			await member.remove_roles(rol)
			await ctx.send(f"{member} Kişisinin {rol} Rolü Kaldırıldı")
			rapor_kanali = self.client.get_channel(int(os.environ.get("LOG_ID")))
		    await rapor_kanali.send(f"{member} Kişisinin {rol} Rolü Kaldırıldı")
		except:
			await ctx.send(f"Bu Kişinin {rol} Rolü Yok")

def setup(client):
	client.add_cog(Rol(client))