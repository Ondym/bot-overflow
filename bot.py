import random
import discord
import os
whiteList = []

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        await message.channel.send('pong')

    if message.content.startswith('<stack'):
        a = random.randint(1000000, 47447511)
        await message.channel.send('https://stackoverflow.com/questions/' + str(a))

    if message.content.startswith('<test'):
        await message.channel.send(client.user)
        await message.channel.send(message.author)

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

client.run('ODAyOTk0Mzc4OTQ3NjkwNTg2.YA3Uyg.wYmoI3VQ2M9cxgJ5ndQcmdPLrDY')
