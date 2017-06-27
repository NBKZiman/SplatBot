#!/usr/bin/env python
# coding: utf-8
import asyncio
import random
import time

import discord

from SplatCalendar import SplatDate, today_holiday_cause, holiday_cause

splat_bot = discord.Client()  # nom du bot


def assert_date(year, month, day):  # une fonction qui vérifie que les dates donné en argument sont bien valide
    if (type(year) is int) and (type(month) is int) and (type(day) is int):
        if (month > 0 and month < 13) and (day > 0 and day < 32):
            return True
    return False


@splat_bot.event
async def on_ready():
    """Indique que le bot est connecté"""
    print('Logged in as')
    print(splat_bot.user.name)
    print(splat_bot.user.id)
    print('------')


@splat_bot.event
async def on_message(message):
    cmd = message.content.split(' ')
    number_option = len(cmd)
    if message.author == splat_bot.user:  # évite que le bot ne se réponde à lui même
        return

    """Definit les reactions aux messages des utilisateurs"""
    if message.content.startswith('!splat'):  # reaction à !splat
        year, month, day, *_ = time.localtime()
        today_splat_date = SplatDate(year, month, day)  # conversion en date splatonique

        if (message.content == '!splat'):
            await splat_bot.send_message(message.channel,
                                         "Nous sommes le {}".format(today_splat_date.formatted_date()))
        elif number_option == 4:
            year_option, month_option, day_option = int(cmd[3]), int(cmd[2]), int(cmd[1])
            if not assert_date(year_option, month_option, day_option) :
                 await splat_bot.send_message(message.channel,
                                              "Go fuck yourself")
            else:
                date_option = (year_option, month_option, day_option, 0, 0, 0, 1, 76, 1)
                futur = (time.mktime(time.localtime()) - time.mktime(date_option) < 0)  # on veut savoir si la date
                # prop# osé en option est une date futur ou passé d'où ce booléen
                if futur:
                    splat_date_option = SplatDate(year_option, month_option, day_option)
                    await splat_bot.send_message(message.channel,
                                                 "Nous serons le {}".format(splat_date_option.formatted_date()))
                else:
                    splat_date_option = SplatDate(year_option, month_option, day_option)
                    await splat_bot.send_message(message.channel,
                                             "Nous étions le {}".format(splat_date_option.formatted_date()))

    if message.content.startswith('!férié'):  # réaction à !Feriés
        if message.content == '!férié':
            holiday_cause_is = today_holiday_cause()
            if holiday_cause_is:
                await splat_bot.send_message(message.channel, "C'est un jour férié : {}".format(holiday_cause_is))
            else:
                await splat_bot.send_message(message.channel, "Ce n'est pas un jour férié")
        elif number_option == 4:
            year_option, month_option, day_option = int(cmd[3]), int(cmd[2]), int(cmd[1])
            if not assert_date(year_option, month_option, day_option):
                await splat_bot.send_message(message.channel,
                                            "Go fuck yourself")
            else:
                holiday_cause_is = holiday_cause(int(cmd[3]), int(cmd[2]), int(cmd[1]))
                if holiday_cause_is:
                    await splat_bot.send_message(message.channel, "C'est un jour férié : {}".format(holiday_cause_is))
                else:
                    await splat_bot.send_message(message.channel, "Ce n'est pas un jour férié")

    if message.content.startswith('!version'):
        await splat_bot.send_message(message.channel, 'Version 1.0.0')


    if message.content.startswith('!help'):
        await splat_bot.send_message(message.channel,
                                     "Les commandes disponibles sont : !splat, !feriés, !seconde, !help, !estCeQueJeDoisFaireG1', !quiEstCe?, !perdu !version, !gitHub et !theGame")


    if message.content.startswith('!seconde'):
        await splat_bot.send_message(message.channel,
                                     "Il s'est écoulé {} secondes depuis le Splat".format(
                                         SplatDate.seconds_since_splat()))

    if message.content.startswith("!estCeQueJeDoisFaireG1'"):
        await splat_bot.send_message(message.channel, 'oui')

    if message.content.startswith('!quiEstCe?'):
        await splat_bot.send_message(message.channel, "C'est moi !! Le Splat Bot")

    if message.content.startswith('!perdu'):
        await splat_bot.send_message(message.channel, "J'ai perdu")

    if message.content.startswith('!ping'):
        await splat_bot.send_message(message.channel, 'Pong')

    if message.content.startswith('!theGame'):
        for _ in range(3):
            temps_aleatoire = random.randint(1, 120)
            await asyncio.sleep(temps_aleatoire)
            await splat_bot.send_message(message.channel, 'Perdu')

    if message.content.startswith('!gitHub'):
        await splat_bot.send_message(message.channel, 'GitHub du Bot : https://github.com/NBKZiman/SplatBot')


splat_bot.run('MzI4NjQ4MDQyMDE2MTQ1NDIw.DDP9MA.f9te3zjYCT-KM1Sg0xq-Izdj3dM')
