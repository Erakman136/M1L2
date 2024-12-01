import discord
from discord.ext import commands
from bot_token import token

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yaptı:  {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Bu discord.py kütüphanesi ile oluşturulmuş echo-bot!')
    
@client.command()
async def add(ctx, sayi1: int = 0, sayi2: int = 0):
    await ctx.send(sayi1 + sayi2)
@client.command()
async def mem(ctx):
    await ctx.send('parantezin türkçedeki etkisi:👌parantezin yazılımdaki etkisi:🌌☀️')
@client.command()
async def yazılım(ctx):
    # Yazılım dilleri listesi
    yazilim_dilleri = {
        "Python": "Python, genel amaçlı bir programlama dilidir ve veri analizi, web geliştirme, yapay zeka gibi birçok alanda kullanılır.",
        "JavaScript": "JavaScript, web geliştirme için popüler bir programlama dilidir ve çoğunlukla tarayıcı üzerinde çalışır.",
        "Java": "Java, çok platformlu uygulamalar geliştirmek için yaygın olarak kullanılan bir dildir.",
        "C#": "C#, Microsoft tarafından geliştirilmiş, oyun geliştirme ve masaüstü uygulamaları için kullanılan bir programlama dilidir.",
        "C++": "C++, yüksek performans gerektiren uygulamalarda tercih edilen güçlü bir dildir."
    }
    
    # Mesajda kullanılan Select Menüsü
    class YazilimSecim(discord.ui.Select):
        def __init__(self):
            options = [
                discord.SelectOption(label=dil, description=f"{dil} hakkında bilgi almak için tıklayın.")
                for dil in yazilim_dilleri.keys()
            ]
            super().__init__(placeholder="Bir yazılım dili seçin...", options=options)

        async def callback(self, interaction: discord.Interaction):
            dil_adi = self.values[0]
            bilgi = yazilim_dilleri.get(dil_adi, "Bu dil hakkında bilgi bulunamadı.")
            await interaction.response.send_message(bilgi, ephemeral=True)

    # View sınıfı
    class YazilimSecimView(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.add_item(YazilimSecim())

    await ctx.send("Hangi yazılım dili hakkında bilgi almak istersiniz?", view=YazilimSecimView())

client.run(token)
