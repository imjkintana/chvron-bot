from discord.ext import commands
from dotenv import load_dotenv
from gameInfo import getGameInfo
import os

load_dotenv('source.env')
# client = discord.Client()
client = commands.Bot(command_prefix = '16.')
client.lastUpdate = getGameInfo()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def lastupdate(ctx):
    await ctx.send(client.lastUpdate)

@client.command()
async def refresh(ctx):
    client.lastUpdate = getGameInfo()
    await ctx.send('Refreshed logs.')

'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        #print(f'In #{message.channel.name}, {message.author.name} triggered "Hello!"')
'''

client.run(os.getenv('TOKEN'))