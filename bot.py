import random
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<ping'):
        await message.channel.send('pong')

    if message.content.startswith('<stack'):
        a = random.randint(1000000, 47447511)
        await message.channel.send('https://stackoverflow.com/questions/' + str(a))

client.run('chtels.token.hejzle')
