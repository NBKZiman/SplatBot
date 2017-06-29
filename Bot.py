#!/usr/bin/env python
# coding: utf-8
import asyncio
import random
import time

import discord

from SplatCalendar import *
from QuoiMangay import *
from HelpRessources import *

splat_bot = discord.Client()  # nom du bot


def assert_date(year: int, month: int, day: int) -> bool:
    """Vérifie que les dates données en arguments sont bien valides, renvoi un booleen"""
    if (type(year) is int) and (type(month) is int) and (type(day) is int):
        if (0 < month < 13) and (0 < day < 32):
            return True
    return False


def assert_bite(cmd, number_option: int) -> bool:
    """Emmpèche les utilisateurs de !bite de mettre trop de lignes, renvoi True si il y a plus de 10
    ligne et/ou 25 aubergine"""
    if number_option > 1:
        if int(cmd[1]) >= 25:
            return True
    if number_option > 2:
        if int(cmd[2]) >= 10 and int(cmd[1]) >= 25:
            return True


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

        if message.content == '!splat':
            await splat_bot.send_message(message.channel,
                                         "Nous sommes le {}".format(today_splat_date.formatted_date()))
        elif number_option == 4:
            year_option, month_option, day_option = int(cmd[3]), int(cmd[2]), int(cmd[1])
            if not assert_date(year_option, month_option, day_option):
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
                                             "Go splat yourself")
            else:
                holiday_cause_is = holiday_cause(int(cmd[3]), int(cmd[2]), int(cmd[1]))
                if holiday_cause_is:
                    await splat_bot.send_message(message.channel, "C'est un jour férié : {}".format(holiday_cause_is))
                else:
                    await splat_bot.send_message(message.channel, "Ce n'est pas un jour férié")

    if message.content.startswith('!version'):
        await splat_bot.send_message(message.channel, 'Version 1.0.0')

    if message.content.startswith('!help'):
        if number_option == 1:
            await splat_bot.send_message(message.channel, get_help('!help'))
        else:
            await splat_bot.send_message(message.channel, get_help(cmd[1]))


    if message.content.startswith('!seconde'):
        await splat_bot.send_message(message.channel,
                                     "Il s'est écoulé {} secondes depuis le Splat".format(
                                         SplatDate.seconds_since_splat()))

    if message.content.startswith("!estCeQueJeVaisFaireG1'"):
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

    if message.content.startswith('!perdu'):
        await splat_bot.send_message(message.channel, 'GitHub du Bot : https://github.com/NBKZiman/SplatBot')

    if message.content.startswith('!bite'):
        if assert_bite(cmd, number_option):
            number_option = 1
        if number_option == 1:
            await splat_bot.send_message(message.channel,
                                         ":eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant:" 
                                         ":eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant:" 
                                         ":eggplant: :eggplant: :eggplant: :eggplant: :eggplant: :eggplant:")

        if number_option == 2:
            egg = ':eggplant: '
            str_long = ' '
            for _ in range(int(cmd[1])):
                str_long = str_long + egg
            await splat_bot.send_message(message.channel, str_long)
        if number_option == 3:
            egg = ':eggplant: '
            str_long = ' '
            for _ in range(int(cmd[1])):
                str_long = str_long + egg
            for _ in range(int(cmd[2])):
                await splat_bot.send_message(message.channel, str_long)

    if message.content.startswith('!mangay'):
        assert number_option <= 3
        if number_option == 1:
            list_mangay = choix_Mangay(' ')
        elif number_option >= 2:
                list_mangay = choix_Mangay(cmd[1])
        if list_mangay == []:
            await splat_bot.send_message(message.channel,
                                         "La catégorie est mauvaise tapez !mangay help pour plus d'info.")
        elif number_option <= 2:
                for i in list_mangay:
                    await splat_bot.send_message(message.channel, i)
        elif cmd[2] == 'hasard':
            random.shuffle(list_mangay)
            await splat_bot.send_message(message.channel, list_mangay[0])

splat_bot.run('MzI4NjQ4MDQyMDE2MTQ1NDIw.DDP9MA.f9te3zjYCT-KM1Sg0xq-Izdj3dM')
