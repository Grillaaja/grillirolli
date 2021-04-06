import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith("!roll"):
        if len(message.mentions) == 1:
            stringi = f'{message.author.mention} {random.randint(1,100)} {message.mentions[0].mention} {random.randint(1,100)}'
            await message.channel.send(stringi , mention_author=True)
        else:
            stringi = str(random.randint(1,100))
            await message.channel.send(stringi)



client.run(os.environ.get("TOKEN"))