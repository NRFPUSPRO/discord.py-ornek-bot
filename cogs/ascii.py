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
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
        print(r.json())    
        
        
        
        
        
        
        
        
def setup(client):
    client.add_cog(Ascii(client))