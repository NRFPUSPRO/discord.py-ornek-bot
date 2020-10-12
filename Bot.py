import discord
from discord.ext import commands
import requests
client = commands.Bot(command_prefix="/")
import os

@client.event
async def on_ready():
	print("Ready")
	
plugins = ["cogs.HitLoggerChecker", "cogs.Ban", "cogs.Unban", "cogs.Kick", "cogs.OtoRol", "cogs.Clear", "cogs.Report", "cogs.Yardım", "cogs.term", "cogs.covid19", "cogs.carbon", "cogs.antikufur"]

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
	giris_cikis_kanali = client.get_channel(int(os.environ.get("GIRIS_CIKIS_ID")))
	await giris_cikis_kanali.send(f"{member.mention} Sunucuya Katıldı Hoş Geldin, Rolün Verildi")
@client.event
async def on_message(message):
        with open("cogs.küfürler.txt") as f:
            for i in f:
                if i in message.content:
                    await message.author.ban()    

client.run(os.environ.get("DISCORD_TOKEN"))
