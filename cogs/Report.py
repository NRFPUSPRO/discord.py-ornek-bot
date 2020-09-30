import discord
from discord.ext import commands


class Report(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def report(self, ctx, kisi, *, reason):
		rapor_kanali = self.client.get_channel(Buraya Raporların Gidiceği Kanalının IDsi Gelmeli "" Olmadan)
		await rapor_kanali.send(f"Rapor Geldi!\nRaporlanan Kişi:\n{kisi}\nRapor Sebebi:\n{reason}")
		await ctx.send("Rapor Gönderildi")


def setup(client):
	client.add_cog(Report(client))
