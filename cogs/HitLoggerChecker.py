from os import error
import discord
from discord.ext import commands
import requests


class HitLoggerChecker(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		#if message.channel.id == 755772621181943879:
		config_url = message.attachments[0].url
		config = requests.get(config_url)
		configi_kaydet = open(f"./{message.attachments[0].filename}", "wb").write(config.content)
		kaydedilen_config = open(f"./{message.attachments[0].filename}", "r")
		for i in kaydedilen_config.readlines():
			if "api.telegram.org" in i:
				await message.author.ban(reason="Hit Loggerlı Config Atmak Yasaktır")
				kaydedilen_config.close()
			elif "discordapp.com/api/webhooks" in i:
				await message.author.ban(reason="Hit Loggerlı Config Atmak Yasaktır")
				kaydedilen_config.close()
			elif "docs.google.com" in i:
				await message.author.ban(reason="Hit Loggerlı Config Atmak Yasaktır")
				kaydedilen_config.close()
			else:
				pass
	@on_message.error
	async def on_message_error(self, error):
		pass
		

def setup(client):
	client.add_cog(HitLoggerChecker(client))
