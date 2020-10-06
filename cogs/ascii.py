import discord
from discord.ext import commands
from requests import post
class Ascii(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command()
    async def ascii(self, ctx, metin):
        
        r = post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': f'{metin}',
        },
        headers={'api-key': 'bd369796-2466-4054-8c35-6feddbcf4711'}
    )
        await ctx.send(r.json()["output_url"])    
        
        
        
        
        
        
        
        
def setup(client):
    client.add_cog(Ascii(client))