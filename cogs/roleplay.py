from sys import prefix
from cogs.help import send_embed
from discord.ext import commands
import random
import requests
import json 
import discord

def get_gif(search):
    search.replace(' ', '+')
    response = requests.get(('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=' + 'lhGgflAeUS0LG3e8YvYYW2JVidrwqcfF' + '&limit=10'))
    data = json.loads(response.text)

    gif_choice = random.randint(0, 9)
    result_gif = data['data'][gif_choice]['images']['original']['url']
    return result_gif

class Reactions(commands.Cog):
    """Reaction for different situations I guess"""
    def __init__(self, client):
        self.client = client

#Send_random_gif
    @commands.command(name='gif')
    async def send_gif(self, ctx, *search):
        """Send Gif by searching"""
        embed = discord.Embed(title='From {}'.format(ctx.author), description='Command: `cock gif {}`'.format(' '.join(search[:])),
                            colour=discord.Colour.blurple())

        embed.set_image(url=get_gif(" ".join(search[:])))  # SET THE IMAGE IN THE EMBED AS THE GIF
        embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/giphy/giphy-logo.png",
                        text="Powered by Giphy")  # SET THE FOOTER WITH THE PROVIDER NAME FOR LEGAL REASONS
        await ctx.send(embed=embed)  # SEND THIS NEW MESSAGE
        await ctx.message.delete()  # DELETE THE ORIGINAL MESSAGE (to make it clean)

#Send_hug
    @commands.command(name='hug', description="Give yourself or your friends a hug!", pass_context=True)
    async def send_hug(self, ctx, mention: discord.User = None):
        if mention == None:
            embed = discord.Embed(title='Oh look {} just gave theirself a hug..'.format(ctx.author),
                                description='Command: `c!hug`',
                                colour=discord.Colour.blurple())
            embed.set_image(url=get_gif('alone+hug'))
            embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/giphy/giphy-logo.png",
                            text="Powered by Giphy")
        else:
            hug_lines = [f'Awww {ctx.author.name} just gave {mention.name} a warm hug!',
                        f"{ctx.author.name} and {mention.name}, Aren't they just the cutest!",
                        f"{ctx.author.name} just gave {mention.name} a BIG hug!"]
            rand_hug_lines = hug_lines[random.randint(0, 2)]
            embed = discord.Embed(title=rand_hug_lines,
                                description='Command: `c!hug {}`'.format(mention),
                                colour=discord.Colour.blurple())
            embed.set_image(url=get_gif('hug'))
            embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/giphy/giphy-logo.png",
                            text="Powered by Giphy")

        await ctx.send(embed=embed)
        await ctx.message.delete()
#Send_suck
    @commands.command(name='suck', description="Suck yehh", pass_context=True, aliases=["succ"])
    async def send_suck(self, ctx, mention: discord.User = None):
        if mention == None:
            embed = discord.Embed(title='Oh look {} just sucked him/herself'.format(ctx.author),
                                description='Command: `cock suck`',
                                colour=discord.Colour.blurple())
            embed.set_image(url=get_gif('suck+finger'))
            embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/giphy/giphy-logo.png",
                            text="Powered by Giphy")
        else:
            suck_lines = [f'Awww {ctx.author.name} just sucked {mention.name}.',
                        f"{ctx.author.name} and {mention.name}, is sucking each other.",
                        f"{ctx.author.name} sucked {mention.name} for free"]
            rand_suck_lines = suck_lines[random.randint(0, 2)]
            embed = discord.Embed(title=rand_suck_lines,
                                description='Command: `cock suck`'.format(mention),
                                colour=discord.Colour.blurple())
            embed.set_image(url=get_gif('suck'))
            embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/giphy/giphy-logo.png",
                            text="Powered by Giphy")

        await ctx.send(embed=embed)
        await ctx.message.delete()

#send_pat
    @commands.command(name='pat', description="just lovely pats", pass_context=True, aliases=["pats"])
    async def send_pat(self, ctx, mention: discord.User = None):
        if mention == None:
            embed = discord.Embed(title='{} pats no one.'.format(ctx.author),
                                description='Command: `cock pat`',
                                colour=discord.Colour.blurple())
            embed.set_image(url=get_gif('cute+pat'))
            embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/giphy/giphy-logo.png",
                            text="Powered by Giphy")
        else:
            embed = discord.Embed(title=f'{ctx.author.name} just patted {mention.name}.',
                                description='Command: `cock pat`'.format(mention),
                                colour=discord.Colour.blurple())
            embed.set_image(url=get_gif('anime+pat'))
            embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/giphy/giphy-logo.png",
                            text="Powered by Giphy")

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name='sex', description="uhh", pass_context=True, aliases=["smex"])
    async def send_sex(self, ctx, mention: discord.User = None):
        if mention == None:
            embed = discord.Embed(title='{} is all alone..'.format(ctx.author),
                                description='Command: `cock sex`',
                                colour=discord.Colour.blurple())
            embed.set_image(url=get_gif('crying+bed'))
            embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/giphy/giphy-logo.png",
                            text="Powered by Giphy")
        else:
            embed = discord.Embed(title=f'{ctx.author.name} SMEX IS BAD!!!!.',
                                description='Command: `cock sex`'.format(mention),
                                colour=discord.Colour.blurple())
            embed.set_image(url=get_gif('slap'))
            embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/giphy/giphy-logo.png",
                            text="Powered by Giphy")

        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Reactions(bot))
