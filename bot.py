import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument
from dotenv import load_dotenv
import os
from cogs.help import send_embed
import zipfile
#1. Load Env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#2. Bot Prefix
client = commands.Bot(command_prefix = "cock ")

#3. Cogs
@client.event
async def on_ready():

    with zipfile.ZipFile('Cookiisha.zip','w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        my_zip.write('../CleanedCookiiSha')

    with zipfile.ZipFile('Cookiisha.zip', 'r') as my_zip:
        print(my_zip.namelist())
@client.event
async def on_command_error(ctx,error):
   if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Missing Required Argument!")
   else:
        raise error
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
        
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
client.run(TOKEN)

#Zip Files 

