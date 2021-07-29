import discord
from discord.ext import commands
from cogs.help import send_embed
import os 
import patoolib
class SendCommands(commands.Cog):
    '''Send commands'''
    def __init__(self, client):
        self.client = client
    @commands.command(name = "send", aliases = ('sendMsg', 'msg'))
    async def send(self, ctx, message):
        """Send a Message `cock send [message]`"""
        await ctx.send(" ".join(message[:]))
        await ctx.message.delete()
            
 
    
    @commands.command(name = "link")
    async def link(self, ctx, title, link_name, link, thumbnail = None):
        """Send a link Embed `cock link [title] [name] (link) [thumbnail - optional]`"""
        if ctx.author.name == "IshaMeii" or ctx.author.name == "RenRen":
            embed = discord.Embed(title = title , description = f"[{link_name}]({link})")
        if thumbnail != None:
            embed.set_thumbnail(url = thumbnail)
        await ctx.message.delete()
        await send_embed(ctx, embed)

    @commands.command(name = 'files')
    async def send_files(self, ctx, message):
        if message == ('main'):
            patoolib.create_archive('main.rar', '../CleanedCookiiSha')

def setup(client):
    client.add_cog(SendCommands(client))
