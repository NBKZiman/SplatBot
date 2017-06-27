#!/usr/bin/env python
# coding: utf-8
import time


class SplatDate:
    """Classe qui convertit une date classique en date splatonique"""
    def __init__(self, year, month, day):
        self.year = year - 2017
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

    def formatted_date(self):
        suffix = "er" if self.day == 1 else ""
        return "{day}{suffix} {month} de l'an {year}".format(day=self.day, suffix=suffix, month=self.month, year=self.year)

    @staticmethod
    def seconds_since_splat():
        t = (2017, 3, 27, 0, 0, 0, 1, 76, 1)
        return time.mktime(time.localtime()) - time.mktime(t)
