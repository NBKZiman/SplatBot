#!/usr/bin/env python
# coding: utf-8
import random
import time

import discord

from SplatCalendar import SplatDate, today_holiday_cause

SplatBot = discord.Client()  # nom du bot


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
        year, month, day, *_ = time.localtime()
        today_splat_date = SplatDate(year, month, day)  # conversion en date splatonique
        await SplatBot.send_message(message.channel,
                                    "Nous sommes le {}".format(today_splat_date.formatted_date()))

    if message.content.startswith('!Feriés'):  # réaction à !Feriés
        holiday_cause = today_holiday_cause()
        if holiday_cause:
            await SplatBot.send_message(message.channel, "C'est un jour férié : {}".format(holiday_cause))
        else:
            await SplatBot.send_message(message.channel, "Ce n'est pas un jour férié")

    if message.content.startswith('!version'):
        await SplatBot.send_message(message.channel, 'Version 0.1.2')

    if message.content.startswith('!help'):
        await SplatBot.send_message(message.channel,
                                    "Les commandes disponibles sont : !splat, !feriés, !seconde, !help, !estCeQueJeDoisFaireG1', !quiEstCe?, !perdu !version, !gitHub et !theGame")

    if message.content.startswith('!seconde'):
        await SplatBot.send_message(message.channel,
                                    "Il s'est écoulé {} secondes depuis le Splat".format(
                                        SplatDate.seconds_since_splat()))

    if message.content.startswith("!estCeQueJeDoisFaireG1'"):
        await SplatBot.send_message(message.channel, 'oui')

    if message.content.startswith('!quiEstCe?'):
        await SplatBot.send_message(message.channel, "C'est moi !! Le Splat Bot")

    if message.content.startswith('!perdu'):
        await SplatBot.send_message(message.channel, "J'ai perdu")

    if message.content.startswith('!ping'):
        await SplatBot.send_message(message.channel, 'Pong')

    if message.content.startswith('!theGame'):
        for _ in range(3):
            temps_aleatoire = random.randint(1, 120)
            time.sleep(temps_aleatoire)
            await SplatBot.send_message(message.channel, 'Perdu @sn00c#3984')

    if message.content.startswith('!gitHub'):
        await SplatBot.send_message(message.channel, 'GitHub du Bot : https://github.com/NBKZiman/SplatBot')


SplatBot.run('MzI4NjQ4MDQyMDE2MTQ1NDIw.DDG-uA.DhcrdS94C2WaZVvLkqOVHV8__O4')
