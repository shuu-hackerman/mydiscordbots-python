import discord
import os

my_secret = os.environ['PREFIX']
my_secret = os.environ['TOKEN']


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Streaming(name='Meu saco', url='https://www.twitch.tv/elemesmocaralho'))

  print('Connected to bot: {}'.format(client.user.name))
  print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&raça'):
        await message.channel.send('Sua raça é')



client.run(os.getenv('TOKEN'))