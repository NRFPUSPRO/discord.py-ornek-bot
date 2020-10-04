import discord
from discord.ext import commands
import requests
import json


class Covid(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def covid(self, ctx):
		req = requests.get("https://api.quiec.tech/corona.php")
		js = json.loads(req.content)
		await ctx.send(f"İşte Güncel Korona Verileri:\nToplam Hasta : {js['tum']}\nToplam Ölüm : {js['tumolum']}\nToplam İyileşen : {js['tumk']}")

	@commands.command()
	async def covidtr(self, ctx):
		req = requests.get("https://api.quiec.tech/corona.php")
		js = json.loads(req.content)
		await ctx.send(f"İşte Türkiyenin Güncel Korona Verileri\nToplam Hasta : {js['trtum']}\nToplam Ölüm : {js['trolum']}\nToplam İyileşen : {js['trk']}")


def setup(client):
	client.add_cog(Covid(client))
