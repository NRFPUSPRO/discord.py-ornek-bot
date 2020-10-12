import discord
from discord.ext import commands

class AntiKufur(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    # @commands.Cog.listener()
    # async def on_message(self, ctx, *, message):
    #     with open("küfürler.txt") as f:
    #         for i in f:
    #             if i in message.content:
    #                 await message.author.ban()    
        
        
        
        
        
        
        
        
def setup(client):
    client.add_cog(AntiKufur(client))