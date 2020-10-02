import discord
from discord.ext import commands
import requests
client = commands.Bot(command_prefix="/")
import os

@client.event
async def on_ready():
	print("Ready")
	
plugins = ["cogs.HitLoggerChecker", "cogs.Ban", "cogs.Unban", "cogs.Kick", "cogs.OtoRol", "cogs.Clear", "cogs.Report", "cogs.Yardım"]

for plugin in plugins:
	client.load_extension(plugin)


@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("Komut Bulunamadı")
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("Bu Komutu Kullanmak İçin Yeterli Yetkiniz Yok")


@client.event
async def on_member_join(member):
	giris_cikis_kanali = os.environ.get("GIRIS_CIKIS_ID")
	await giris_cikis_kanali.send(f"{member.mention} Sunucuya Katıldı Hoş Geldin, Rolün Verildi")


client.run(os.environ.get("DISCORD_TOKEN"))
