"""Définit un tour."""

import time

class Round:
    def __init__(self, name, beginning_date, ending_date):
        """Initialise un tour."""
        self.name =  name
        self.beginning_date = beginning_date
        self.ending_date = ending_date
        self.matchs_list = []


def create_round(i):
    '''Préparation des attributs d'un tour.'''
    name = f'Round {i+1}'
    beginning_date = '{}'.format(time.strftime("%Y-%m-%d_%Hh"))
    ending_date = ''
    round = Round(name, beginning_date, ending_date)

    return round
