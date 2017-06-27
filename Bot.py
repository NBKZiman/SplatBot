import discord
import asyncio
import time
import random

SplatBot = discord.Client() # nom du bot

def SplatDate(annee,mois,jour):
    '''Fonction qui convertie une date classique en date splatonique'''
    Smois = 0
    Sjour = 0
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
            Sjour = jour -24 +2
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
    if message.author == SplatBot.user:
        return
    '''definie les reactions aux messages des utilistateurs'''
    if message.content.startswith('!splat'): # reaction a !splat
        if message.content == '!splat' :
            year = time.localtime()[0]
            month = time.localtime()[1]
            day = time.localtime()[2]
            Splat = SplatDate(year, month,day) # conversion en date splatonique
            if Splat[2] ==  1:
                await SplatBot.send_message(message.channel, 'Nous sommes le ' + str(Splat[2]) + 'er ' + str(Splat[1]) + ' de l\'an ' + str(Splat[0])) # affichage du message
            else :
                await SplatBot.send_message(message.channel,'Nous sommes le ' + str(Splat[2]) + ' ' + str(Splat[1]) + ' de l\'an ' + str(Splat[0]))
        else :
            rawmess = message.content.split(' ')
            assert len(rawmess) == 4
            Splat = SplatDate(int(rawmess[3]), int(rawmess[2]), int(rawmess[1]))  # conversion en date splatonique
            if Splat == (0, 0, 0):
                await SplatBot.send_message(message.channel, 'Le Splatendrier n\'existait pas a ce moment là')
            elif Splat[2] == 1:
                await SplatBot.send_message(message.channel, 'Nous étions le ' + str(Splat[2]) + 'er ' + str(Splat[1]) + ' de l\'an ' + str(Splat[0]))  # affichage du message
            else :
                await SplatBot.send_message(message.channel, 'Nous étions le ' + str(Splat[2]) + ' ' + str(Splat[1]) + ' de l\'an ' + str(Splat[0]))

    if message.content.startswith('!fériés'): # réaction a !ferie
        a = estFerie()
        if a[0]==True :
             await SplatBot.send_message(message.channel, 'C\'est un jour ferié : ' + FerieCause[a[1]])
        else :
            await SplatBot.send_message(message.channel, 'Ce n\'est pas un jour ferié')

    if message.content.startswith('!version'):
        await SplatBot.send_message(message.channel, 'Version 0.1.2')

    if message.content.startswith('!seconde'):
        t = (2017, 3, 27, 20, 0, 0, 1, 76, 1)
        a = time.mktime(time.localtime()) - time.mktime(t)
        await SplatBot.send_message(message.channel, 'il s\'est écoulé ' + str(a) + ' secondes depuis le Splat')

    if message.content.startswith('!estCeQueJeDoisFaireG1\''):
        await SplatBot.send_message(message.channel, 'Oui')

    if message.content.startswith('!quiEstCe?'):
        await SplatBot.send_message(message.channel, 'C\'est moi !! Le Splat Bot')

    if message.content.startswith('!perdu'):
        await SplatBot.send_message(message.channel, 'J\'ai perdu')

    if message.content.startswith('!ping'):
        await SplatBot.send_message(message.channel, 'Pong')

    if message.content.startswith('!theGame'):
        for i in range(3):
            tempsAleatoire = random.randint(1, 30)
            time.sleep(tempsAleatoire)
            await SplatBot.send_message(message.channel, 'Perdu')

    if message.content.startswith('!gitHub'):
        await SplatBot.send_message(message.channel, 'GitHub du Bot : https://github.com/NBKZiman/SplatBot')

    if message.content.startswith('!Bite'):
        fmt = '-%/%| /n                 _,-\'   \//%\ /n            _,-\'        \%/|% /n          / / )    __,--  /%\ /n          \__/_,-\'%(%  ;  %)% /n                  %\%,   %\ /n                    \'--%\' /n '
        await SplatBot.send_message(message.channel, fmt.format())

    if message.content.startswith('!mangay'):
        rawmess = message.content
        if rawmess == '!mangay' :
            await SplatBot.send_message(message.channel, 'Votez pour ce que vous voulez manger :')
            await SplatBot.send_message(message.channel, 'Italia Pizza')
            await SplatBot.send_message(message.channel, 'Kebab')
            await SplatBot.send_message(message.channel, 'Urban Burger')
            await SplatBot.send_message(message.channel, 'Café des délices')
            await SplatBot.send_message(message.channel, 'Asian')
            await SplatBot.send_message(message.channel, 'Salad&Co')
            await SplatBot.send_message(message.channel, 'Mac Donalds')
            await SplatBot.send_message(message.channel, 'Memphis')
            await SplatBot.send_message(message.channel, 'Burger King')
            await SplatBot.send_message(message.channel, 'KFC')
            await SplatBot.send_message(message.channel, 'Mange chez toi')
        if 'commande' in rawmess.split(' ') and not 'hasard' in rawmess.split(' '):
            await SplatBot.send_message(message.channel, 'Votez pour ce que vous voulez manger :')
            await SplatBot.send_message(message.channel, 'Italia Pizza')
            await SplatBot.send_message(message.channel, 'Kebab')
            await SplatBot.send_message(message.channel, 'Urban Burger')
            await SplatBot.send_message(message.channel, 'Café des délices')
            await SplatBot.send_message(message.channel, 'Mange chez toi')
        if 'cher' in rawmess.split(' ') and not 'hasard' in rawmess.split(' '):
            await SplatBot.send_message(message.channel, 'Votez pour ce que vous voulez manger :')
            await SplatBot.send_message(message.channel, 'Asian')
            await SplatBot.send_message(message.channel, 'Salad&Co')
            await SplatBot.send_message(message.channel, 'Mac Donalds')
            await SplatBot.send_message(message.channel, 'Memphis')
            await SplatBot.send_message(message.channel, 'Burger King')
            await SplatBot.send_message(message.channel, 'KFC')
            await SplatBot.send_message(message.channel, 'Mange chez toi')
        if 'resto' in rawmess.split(' ') and not 'hasard' in rawmess.split(' '):
            await SplatBot.send_message(message.channel, 'Votez pour ce que vous voulez manger :')
            await SplatBot.send_message(message.channel, 'Asian')
            await SplatBot.send_message(message.channel, 'Salad&Co')
            await SplatBot.send_message(message.channel, 'Memphis')
            await SplatBot.send_message(message.channel, 'Mange chez toi')
        if 'fastfood' in rawmess.split(' ') and not 'hasard' in rawmess.split(' '):
            await SplatBot.send_message(message.channel, 'Votez pour ce que vous voulez manger :')
            await SplatBot.send_message(message.channel, 'Burger King')
            await SplatBot.send_message(message.channel, 'KFC')
            await SplatBot.send_message(message.channel, 'Kebab')
            await SplatBot.send_message(message.channel, 'Italia Pizza')
            await SplatBot.send_message(message.channel, 'Mange chez toi')
        if 'commande' in rawmess.split(' ') and 'hasard' in rawmess.split(' ') :
            mange = random.randint(1, 4)
            if mange == 1:
                await SplatBot.send_message(message.channel, 'Italia Pizza')
            elif mange == 2:
                await SplatBot.send_message(message.channel, 'Kebab')
            elif mange == 3:
                burger = random.randint(0, 1)
                if burger == 0:
                    await SplatBot.send_message(message.channel, 'Urban Burger')
                else:
                    await SplatBot.send_message(message.channel, 'Café des délices')
            elif mange == 4:
                await SplatBot.send_message(message.channel, 'Mange chez toi')
        if 'cher' in rawmess.split(' ')  and 'hasard' in rawmess.split(' '):
            mange = random.randint(1, 5)
            if mange == 1:
                await SplatBot.send_message(message.channel, 'Asian')
            elif mange == 2:
                await SplatBot.send_message(message.channel, 'Salad&Co')
            elif mange == 3:
                await SplatBot.send_message(message.channel, 'Mac Donalds')
            elif mange == 4:
                await SplatBot.send_message(message.channel, 'Memphis')
            elif mange == 4:
                await SplatBot.send_message(message.channel, 'Burger King')
            elif mange == 5:
                await SplatBot.send_message(message.channel, 'KFC')


    if message.content.startswith('!bite'):
        rawmess = message.content
        n = len(rawmess.split(' '))
        if n > 1 :
            if int(rawmess.split(' ')[1]) >= 25 or int(rawmess.split(' ')[2]) >=10 :
                 n = 1
        if n == 1 :
            await SplatBot.send_message(message.channel, ':eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant:')
        if n >= 2 :
            egg = ':eggplant: '
            str_long = ' '
            for i in range(int(rawmess.split(' ')[1])):
                str_long = str_long + egg
            await SplatBot.send_message(message.channel, str_long)
        if n == 3 :
            egg = ':eggplant:'
            str_long = ' '
            for i in range(int(rawmess.split(' ')[1])):
                str_long = str_long + egg
            for i in range(int(rawmess.split(' ')[2])) :
                await SplatBot.send_message(message.channel, str_long)

    if message.content.startswith('!tibo'):
        member = discord.utils.find(lambda m: m.name == 'Dreamy', discord.Channel.server.members)
        fmt = '{0.mention} ELLE SONT OÙ LES PIZZZZAAAAASSSSS'
        await SplatBot.send_message(message.channel, fmt.format(member))

    if message.content.startswith('!blague'):
        await SplatBot.send_message(message.channel, 'lel')

    if message.content.startswith('!help'):
        rawmess = message.content
        if rawmess == '!help' :
            await SplatBot.send_message(message.channel, 'Les commandes disponibles sont : !splat, !feriés, !seconde, !help, !estCeQueJeDoisFaireG1\', !quiEstCe?, !perdu !version, !gitHub, !blague et !theGame \n Tapez !help <commande> pour avoir plus d\'information')
        if rawmess == '!help splat' :
            await SplatBot.send_message(message.channel, 'Affiche la date selon le Splatendar')
        if rawmess == '!help fériés' :
            await SplatBot.send_message(message.channel, 'Détermine si le jour actuel est un jour ferié')
        if rawmess == '!help seconde' :
            await SplatBot.send_message(message.channel, 'Affiche le nombre de secondes écoulé depuis le saint Splat')
        if rawmess == '!help estCeQueJeDoisFaireG1\'' :
            await SplatBot.send_message(message.channel, 'Renvoi oui parce que tu ne dois pas avoir d\'espoir')
        if rawmess == '!help quiEstCe' :
            await SplatBot.send_message(message.channel, 'Le SplatBot se présente')
        if rawmess == '!help blague' :
            await SplatBot.send_message(message.channel, 'Le Bot rigole à la dernère blague faite')
        if rawmess == '!help bite' :
            await SplatBot.send_message(message.channel, 'Affiche des aubergines <nombre d\'aubergine><nombre de ligne>. Le maximum d\' aubergine par ligne est de 35 et le maximum de ligne est de 10.')
        if rawmess == '!help mangay':
            await SplatBot.send_message(message.channel, '!mangay [commande, cher, resto, fastfood] [hasard]. donne la liste des lieux où l\'on peut mmanger selon les catégories, il suffit ensuite de voter. Par défaut tous les endroits sont affichés. Option commande pour les endroits qui livrent seulement, option cher pour les endroits pour lesquels il faut se déplacer, .... L\'option hasard permet de tirer un endroit au hasard (ne marche qu\'avec cher et commande pur le moment.')
        if rawmess == '!help !version' :
            await SplatBot.send_message(message.channel, 'Donne la version du bot')

SplatBot.run('MzI4NjQ4MDQyMDE2MTQ1NDIw.DDG-uA.DhcrdS94C2WaZVvLkqOVHV8__O4')