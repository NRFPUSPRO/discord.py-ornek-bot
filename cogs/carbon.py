import discord
from discord.ext import commands
import os
import requests
import urllib.parse

class Carbon(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def carbon(self, ctx, *, kod):
		urlkod = urllib.parse.quote_plus(kod)
		if os.path.exists("Carbon-Kod.jpg"):
			os.remove("Carbon-Kod.jpg")
		if len(kod) < 1:
			await ctx.send('Kullanım "/carbon kod" Şeklindedir')
		req = requests.get(f"https://carbonnowsh.herokuapp.com/?code={urlkod}")

		with open("Carbon-Kod.jpg", 'wb') as f:
			f.write(req.content)
		await ctx.send(file=discord.File('Carbon-Kod.jpg'))


def setup(client):
	client.add_cog(Carbon(client))
