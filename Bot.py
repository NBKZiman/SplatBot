import discord
import asyncio
import time
import random

SplatBot = discord.Client() # nom du bot

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
        if Splat[2] ==  1:
            await SplatBot.send_message(message.channel, 'Nous sommes le ' + str(Splat[2]) + 'er ' + str(Splat[1]) + ' de l\'an ' + str(Splat[0])) # affichage du message
        else :
            await SplatBot.send_message(message.channel,'Nous sommes le ' + str(Splat[2]) + ' ' + str(Splat[1]) + ' de l\'an ' + str(Splat[0]))

    if message.content.startswith('!Feriés'): # réaction a !ferie
        a = estFerie()
        if a[0]==True :
             await SplatBot.send_message(message.channel, 'C\'est un jour ferié : ' + FerieCause[a[1]])
        else :
            await SplatBot.send_message(message.channel, 'Ce n\'est pas un jour ferié')

    if message.content.startswith('!version'):
        await SplatBot.send_message(message.channel, 'Version 0.1.2')

    if message.content.startswith('!help'):
        await SplatBot.send_message(message.channel, 'Les commandes disponibles sont : !splat, !feriés, !seconde, !help, !estCeQueJeDoisFaireG1\', !quiEstCe?, !perdu !version, !gitHub et !theGame')

    if message.content.startswith('!seconde'):
        t = (2017, 3, 27, 0, 0, 0, 1, 76, 1)
        a = time.mktime(time.localtime()) - time.mktime(t)
        await SplatBot.send_message(message.channel, 'il s\'est écoulé ' + str(a) + ' secondes depuis le Splat')

    if message.content.startswith('!estCeQueJeDoisFaireG1\''):
        await SplatBot.send_message(message.channel, 'oui')

    if message.content.startswith('!quiEstCe?'):
        await SplatBot.send_message(message.channel, 'C\'est moi !! Le Splat Bot')

    if message.content.startswith('!perdu'):
        await SplatBot.send_message(message.channel, 'J\'ai perdu')

    if message.content.startswith('!ping'):
        await SplatBot.send_message(message.channel, 'Pong')

    if message.content.startswith('!theGame'):
        for i in range(3):
            tempsAleatoire = random.randint(1, 120)
            time.sleep(tempsAleatoire)
            await SplatBot.send_message(message.channel, 'Perdu @sn00c#3984')

    if message.content.startswith('!gitHub'):
        await SplatBot.send_message(message.channel, 'GitHub du Bot : https://github.com/NBKZiman/SplatBot')



SplatBot.run('MzI4NjQ4MDQyMDE2MTQ1NDIw.DDG-uA.DhcrdS94C2WaZVvLkqOVHV8__O4')