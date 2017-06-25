import discord
import asyncio
import time

SplatBot = discord.Client() # nom du bot

@SplatBot.event
async def on_ready():
    '''Indique que le bot est connecte'''
    print('Logged in as')
    print(SplatBot.user.name)
    print(SplatBot.user.id)
    print('------')

@SplatBot.event
async def on_message(message):
    '''definie les reactions aux messages des utilistateurs'''
    if message.content.startswith('!splat'): # reaction a !splat
        year = time.localtime()[0]
        month = time.localtime()[1]
        day = time.localtime()[2]
        Splat = SplatDate(year, month,day) # conversion en date splatonique
        await SplatBot.send_message(message.channel, 'Nous sommes le' + Splat[0] + 'ème' + Splat[1] + ' de l an' + Splat[2]) # affichage du message

async def on_message(message):
    if message.content.startswith('!feriés'): # réaction a !ferie
        a = estFerie()
    if a[0]==True :
        await SplatBot.send_message(message.channel, 'C est un jour ferié : ' + FerieCause[a[1]])
    else :
        await SplatBot.send_message(message.channel, 'Ce n est pas un jour ferié')

SplatBot.run('Your_Token_Here')

def SplatDate(annee,mois,jour):
    '''Fonction qui convertie une date classique en date splatonique'''
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
    if mois == 5 :
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
    return (annee, Smois, Sjour)

FerieDate = [['Gvrier', 1], ['Gevrier', 1], ['Gevrier', 2]] #tableau des jours feries
FerieCause = ['Le Splat', 'Hell-a-J', 'Hell-a-J'] # Tableau des noms des jours feries

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