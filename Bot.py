import discord
import asyncio
import time
import random

SplatBot = discord.Client()  # nom du bot


class SplatDate:
    """Classe qui convertit une date classique en date splatonique"""
    def __init__(self, year, month, day):
        self.year = 0
        if month == 3:
            if day >= 27:
                self.month = 'Givier'
                self.day = day - 27 + 1
        if month == 4:
            if day < 29:
                self.month = 'Givier'
                self.day = day + 5
            else:
                self.month = 'Fevrilyo'
                self.day = day - 29 + 1
        if month == 5:
            if day < 14:
                self.month = 'Fevrilyo'
                self.day = day + 2
            else:
                self.month = 'Maikkar'
                self.day = day - 15 + 1
        if month == 6:
            if day < 23:
                self.month = 'Markkos'
                self.day = day + 18 - 1
            else:
                self.month = 'Avrylocus'
                self.day = day - 24


FerieDate = [['Gvrier', 1], ['Gevrier', 1], ['Gevrier', 2]]  # tableau des jours fériés
FerieCause = ['Le Splat', 'Hell-a-J', 'Hell-a-J']  # Tableau des noms des jours fériés


def estFerie():
    year = time.localtime()[0]
    month = time.localtime()[1]
    day = time.localtime()[2]
    splat_date = SplatDate(year, month, day)
    for i in range(len(FerieDate)):
        if (splat_date.month == FerieDate[i][1] and splat_date.day == FerieDate[3]):
            return (True, i)
        else:
            return (False, -1)


@SplatBot.event
async def on_ready():
    """Indique que le bot est connecté"""
    print('Logged in as')
    print(SplatBot.user.name)
    print(SplatBot.user.id)
    print('------')


@SplatBot.event
async def on_message(message):
    """Definit les reactions aux messages des utilisateurs"""
    if message.content.startswith('!splat'):  # reaction à !splat
        year = time.localtime()[0]
        month = time.localtime()[1]
        day = time.localtime()[2]
        splat_date = SplatDate(year, month, day)  # conversion en date splatonique
        if splat_date.day == 1:
            await SplatBot.send_message(message.channel,
                                        'Nous sommes le ' + str(splat_date.day) + 'er ' + str(splat_date.month) + ' de l\'an ' + str(
                                            splat_date.year))  # affichage du message
        else:
            await SplatBot.send_message(message.channel,
                                        'Nous sommes le ' + str(splat_date.day) + ' ' + str(splat_date.month) + ' de l\'an ' + str(
                                            splat_date.year))

    if message.content.startswith('!Feriés'):  # réaction à !Feriés
        a = estFerie()
        if a[0]:
            await SplatBot.send_message(message.channel, 'C\'est un jour férié : ' + FerieCause[a[1]])
        else:
            await SplatBot.send_message(message.channel, 'Ce n\'est pas un jour férié')

    if message.content.startswith('!version'):
        await SplatBot.send_message(message.channel, 'Version 0.1.2')

    if message.content.startswith('!help'):
        await SplatBot.send_message(message.channel,
                                    'Les commandes disponibles sont : !splat, !feriés, !seconde, !help, !estCeQueJeDoisFaireG1\', !quiEstCe?, !perdu !version, !gitHub et !theGame')

    if message.content.startswith('!seconde'):
        t = (2017, 3, 27, 0, 0, 0, 1, 76, 1)
        a = time.mktime(time.localtime()) - time.mktime(t)
        await SplatBot.send_message(message.channel, 'Il s\'est écoulé ' + str(a) + ' secondes depuis le Splat')

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
