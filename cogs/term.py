import discord
from discord.ext import commands
import asyncio
from getpass import getuser
from os import remove
import os

class System(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def term(self, ctx, *, command):
		try:
			from os import geteuid
			uid = geteuid()
		except ImportError:
			uid = "Bu değil şef!"
		currusr = getuser()

		process = await asyncio.create_subprocess_shell(
			command,
			stdout=asyncio.subprocess.PIPE,
			stderr=asyncio.subprocess.PIPE)
		stdout, stderr = await process.communicate()
		result = str(stdout.decode().strip()) \
				 + str(stderr.decode().strip())

		if len(result) > 2000:
			output = open("output.txt", "w+")
			output.write(result)
			output.close()
			await ctx.send("Çıktı Çok Büyük Dosya Olarak Gönderiliyor", file=discord.File("output.txt"))
			remove("output.txt")
			return

		if uid == 0:
			await ctx.send(f"{currusr}:~# {command}" f"\n{result}")
		else:
			await ctx.send(f"{currusr}:~$ {command}" f"\n{result}")

		rapor_kanali = self.client.get_channel(int(os.environ.get("LOG_ID")))
		await rapor_kanali.send(f"{command} Komutu Çalıştırıldı")


def setup(client):
	client.add_cog(System(client))
