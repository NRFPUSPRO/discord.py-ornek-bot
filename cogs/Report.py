import discord
from discord.ext import commands
import os

class Report(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def report(self, ctx, kisi, *, reason):
		rapor_kanali = os.environ.get("LOG_ID")
		await rapor_kanali.send(f"Rapor Geldi!\nRaporlanan Kişi:\n{kisi}\nRapor Sebebi:\n{reason}")
		await ctx.send("Rapor Gönderildi")


def setup(client):
	client.add_cog(Report(client))
