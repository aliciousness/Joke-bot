import discord,os,requests
from jokeapi import Jokes

client = discord.Client()
token = os.environ['TOKEN']
funnyApi = requests.get('https://v2.jokeapi.dev/joke/Any?format=txt&type=single')
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  
  if message.content.startswith('$tell me a joke'):
      j = await Jokes()
      await j.get_joke()
      if joke["type"] =='single':
          await message.channel.send(joke['joke'])  


client.run(token)