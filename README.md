discord.py-ornek-bot
Discord.py İçin Küçük Bir Altyapıdır 

Eğer Kodlarla Değilde Botun Kendisiyle İlgileniyorsanız Kolayca Kendi Botunuza Entegre Edebilirsiniz.

İlk Olarak heroku.com Da Bir Üyelik Oluşturmalısınız.

Daha  Sonra https://discord.com/developers/applications Adresinden New Application Butonuna Basarak

Yeni Bir Uygulama Oluşturmalı ve O Uygulamanın Üstüne Bastıktan Sonra Sol Taraftaki Menüden Bot 

Sekmesine Gitmeli ve Add Bot Butonuna Basıp Yeni Bir Bot Oluşturmalısınız Burada Bize Lazım Olan 

Kısım TOKEN Kısmıdır Oradaki Copy Butonuna Basıp Kopyalanan Tokeni Bir Yere Kaydedin Bu Token 

Önemlidir Kimseyle Paylaşmayın.

Daha Sonra İse Botun Giriş Çıkış Mesajlarını Atıcağı Kanalın IDsini Almamız Gerekiyor Yapmamız Gerekenler Şunlar:

1) Discord Uygulamasının Ayarlar Bölümüne Gelin ve Görünüm Sekmesinden Geliştirici Modunu Açın.
2) Giriş Çıkış Kanalı Olarak Kullanılıcak Bir Kanal Oluşturun Ve O Kanalın Üstüne Sağ Tıklayıp ID!yi Kopyala Seçeneğini Seçin.
3) Bunu Bir Yere Kaydedin. 

Daha Sonra İse Botun Yaptığı Şeyleri Kayıt Altına Alıcağı Kanalın IDsini ALmamız Gerekiyor Yapıcaklarımız Neredeyse Aynı :

1) Log Kanalı Olarak Kullanılıcak Bir Kanal Oluşturun.
2) Kanala Sağ Tıklayıp ID'yi Kopyala Seçeneğini Seçin.

Ayarlamalarımız Bitti Kurmayaya Geçebiliriz 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/NRFPUSPRO/discord.py-ornek-bot)

Yukardıdaki Butona Tıklayın 

1) App Name Kısmına İstediğiniz Bir  İsmi Verin

2) DISCORD_TOKEN Kısmına Discorddan Aldığınız Tokeni Girin

3) GIRIS_CIKIS_ID Kısmına Giriş Çıkış Kanalının ID'sini Girin

4) LOG_ID Kısmına Log Kanalının ID'sini Girin

5) ROL_ADI Kısmına Bir Üye Katıldığında Otomatik Olarak Verilicek Rolu Girin ROL DAHA ÖNCE OLUŞTURULMUŞ OLMALIDIR.

6) Deploy Butonuna Basın Ve Manage App Butonu Çıkana Kadar Bekleyin 

7) Manage App Butonuna Basın

8) Çıkan Ekrandan Resources Kısmına Gelin

9) worker python Bot.py Yazan Kısmın Sağındaki Kalem İşaretine Basın Ve Düğmeyi Açın 

10) Birkaç Saniye Bekleyin Ve İşlem Tamam

11) Botun En İyi Şekilde Çalışması İçin Bota Administrator Yetkisi Vermenizi Öneririm


Not : Botu Sunucuya Eklemek İçin : https://discord.com/developers/applications/ Adresine Gelin Uygulamanıza Basın Oradaki Menüden OAuth2 Butonuna Basın Scopes Kısmını bot BOT PERMISSIONS Kısmını Da Administrator Seçin Ve Çıkan URl'i Kopyalayıp Tarayıcıda Açın Ve Sunucunuza Ekleyin

Not 2 : Eğer Otorol Çalışmıyorsa Oto Vermesini İstediğiniz Rolü Silip Tekrar Oluşturun.