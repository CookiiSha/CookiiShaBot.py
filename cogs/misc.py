from sys import prefix
from cogs.help import send_embed
from discord.ext import commands
import random
import discord

class Miscellaneous(commands.Cog):
    """Idk how it's spelled but Miscellaneous"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.client} is Online!')
        


    @commands.command(name="8ball", description="Ask Questions and find Answers")
    async def _8ball(self, ctx, *message):
        rng = random.randint(0, 7)
        eight_ball = [ "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
        await ctx.send(f'>>> Question: `{" ".join(message[:])}`\nAnswer: `{eight_ball[rng]}`')
    @commands.command()
    async def ping(self, ctx):
        """Send a ping"""
        await ctx.send('Pong')
    
        
    @commands.command(name="size", description="cocksize")
    async def size(self, ctx):
        """REVEAL THEI COCK SIZE"""
        cock = "8"
        cock_size = random.randint(0, 50)
        cock_sizes = cock_size
        while(cock_sizes > 0):
            cock_sizes-=1
            cock += "="
        cock+="D"
        if cock_size > 40:
            embed = discord.Embed(title="COOOOOOOOOOCK!!!!",
                    description=cock,
                    color=discord.Color.dark_grey())
        elif cock_size > 30:
            embed = discord.Embed(title="COCK!!!",
                    description=cock,
                    color=discord.Color.dark_grey())
        elif cock_size > 20:
            embed = discord.Embed(title="COCK",
                    description=cock,
                    color=discord.Color.dark_grey())
        elif cock_size > 10:
            embed = discord.Embed(title="just cock",
                    description=cock,
                    color=discord.Color.dark_grey())
        else:
            embed = discord.Embed(title="cock..",
                    description=cock,
                    color=discord.Color.dark_grey())
        await send_embed(ctx, embed)

    async def on_message(self, message):
        word_list = ['fuck', 'frick', 'shit', 'hoe']

        # don't respond to ourselves
        if message.author == self.user:
            return

        messageContent = message.content
        if len(messageContent) > 0:
            for word in word_list:
                if word in messageContent:
                    print(message)
                    await message.delete()
                    await message.channel.send("Succesfully Removed Inappropriate Message!")


def setup(client):
    client.add_cog(Miscellaneous(client))
