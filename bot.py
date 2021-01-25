import random
import discord
import os
import requests
import json
from urllib.request import urlopen
whiteList = []

client = discord.Client()

@client.event
async def on_ready():
    print('Connected as {0.user}'.format(client))
    print("If you don't see any error, {0.user} is ready".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        await message.channel.send('pong')

    if message.content.startswith('<stack'):
        a = random.randint(1000000, 9999064)
        await message.channel.send('https://stackoverflow.com/questions/' + str(a))

    # if message.content.startswith('<test'):

    if message.content.startswith('<add'):
        try:
            whiteList.index(message.author)
        except:
            whiteList.append(message.author)
            await message.channel.send("Sukcesfuli edyt " + str(message.author))
        else:
            await message.channel.send("❌ Jú ár alredy on d vajtlist")
    if message.content.startswith('<del'):
        try:
            whiteList.pop(whiteList.index(message.author))
        except:
            await message.channel.send("❌ Jú árent on d vajtlist")
        else:
            await message.channel.send("Dylít vós sukcefl")
    if message.content.startswith('<check'):
        await message.channel.send(whiteList)

    if message.content.startswith('<help'):
        try:
            whiteList.index(message.author)
        except:
            await message.channel.send('no help for you, becuz yur not on d wajtlist')
        else:
            await message.channel.send('hýr iz help fór jú')
    if message.content.startswith('<find'):
        url=str(message.content)
        url=url[6:len(url)]
        url = url.replace(" ", "+")
        url = "https://stackoverflow.com/search?q=" + url
        page = urlopen(url)
        html = page.read().decode("utf-8")
        await message.channel.send(html[0:2000])


client.run('interesting')
