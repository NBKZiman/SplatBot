import discord
import asyncio
import time

SplatBot = discord.Client()

@SplatBot.event
async def on_ready():
    print('Logged in as')
    print(SplatBot.user.name)
    print(SplatBot.user.id)
    print('------')

@SplatBot.event
async def on_message(message):
    if message.content.startswith('!splat'):
        year = time.localtime()[0]
        month = time.localtime()[1]
        day = time.localtime()[2]
        Splat = SplatDate(year, month,day)
        await client.send_message(message.channel, 'Nous sommes le' + Splat[0] + 'ème' + Splat[1] + ' de l an' + Splat[2])

async def on_message(message):
    if message.content.startswith('!feriés'):
    estFerie() = (a, b)
    if a==True :
        await client.send_message(message.channel, 'C est un jour ferié : ' + FerieCause[b])
    else :
        await client.send_message(message.channel, 'Ce n est pas un jour ferié')

client.run('Your_Token_Here')

def SplatDate(annee,mois,jour):
    annee = 0
    if mois == 3 :
        if jour >= 27 :
            Smois = 'Givier'
            Sjour = jour - 27 + 1
    if mois == 4 :
        if jour < 29 :
            Smois = 'Givier'
            Sjour = jour + 5
        else :
            Smois = 'Fevrilyo'
            Sjour = jour - 29 + 1
    if mois == 5
        if jour < 14 :
            Smois = 'Fevrilyo'
            Sjour = jour + 2
        else :
            Smois = 'Maikkar'
            Sjour = jour - 15 + 1
    if  mois == 6 :
        if jour < 23 :
            Smois = 'Markkos'
            Sjour = jour + 18 - 1
        else :
            Smois = 'Avrylocus'
            Sjour = jour -24
    return (0, Smois, Sjour)

FerieDate = [['Gvrier', 1], ['Gevrier', 1], ['Gevrier', 2]]
FerieCause = ['Le Splat', 'Hell-a-J', 'Hell-a-J']

def estFerie():
    year = time.localtime()[0]
    month = time.localtime()[1]
    day = time.localtime()[2]
    Splat = SplatDate(year, month, day)
    for i in range (len(FerieDate)):
        if (Splat[1]==FerieDate[i][1] and Splat[2]==FerieDate[3]):
            return (True, i)
        else :
            return (False, -1)