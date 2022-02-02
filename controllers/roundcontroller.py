import time
from models.round import Round

def create_round(i):
    '''Préparation des attributs d'un tour.'''
    name = f'Round {i+1}'
    beginning_date = '{}'.format(time.strftime("%Y-%m-%d_%Hh"))
    ending_date = ''
    round = Round(name, beginning_date, ending_date)

    return round

def create_ending_round_date(self):
    self.ending_date = '{}'.format(time.strftime("%Y-%m-%d_%Hh"))