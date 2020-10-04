import discord
from discord.ext import commands


class Yardım(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def yardım(self, ctx):
		await ctx.send(f"Merhaba,\nŞu Anlık Komutlarım Şunlar:\nBan : Kullanıcıyı Banlar (Sadece Adminler)\nUnban : Kullanıcının Banını Kaldırır (Sadece Adminler)\nKick : Kullanıcıyı Sunucudan Atar (Sadece Adminler)\nClear : Belirtilen Sayı Kadar Mesajı Temizler (Sadece Adminler)\nReport : Belirttiğiniz Kişiyi Adminlere Raporlar (Kullanımı /report kullanıcıadı sebebi Şeklindedir)\nTerm : Sunucuda Terminal Komutları Çalıştırmak İçindir (Sadece Adminler)\nCovid : Dünyadaki Korona Verilerini Gösterir\nCovidtr : Türkiyedeki Korona Verilerini Gösterir\nCarbon : Verdiğiniz Metni Şekilli Şukullu Yapar\nYardım : Bu Mesajı Görüntüler")


def setup(client):
	client.add_cog(Yardım(client))
