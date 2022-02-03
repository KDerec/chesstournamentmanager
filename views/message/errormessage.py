"""Displays error messages."""


def display_wrong_choice_message():
    print('!! Vous n\'avez pas choisi un chiffre valide. !!')


def display_not_an_integer_message():
    print('!! Vous n\'avez pas choisi un nombre entier. !!')


def display_not_an_integer_or_float_number():
    print('!! Vous n\'avez pas choisi un nombre entier ou à virgule. !!')


def display_its_blank_message():
    print('!! Vous n\'avez pas saisie de texte. !!')


def display_not_in_selection_range():
    print('!! Vous n\'avez pas saisie un numéro de la sélection valide. !!')


def display_not_positive_integer():
    print('!! Vous n\'avez pas saisie un entier positif. !!')


def display_not_possible_birthday_date():
    print('''Vous n\'avez pas saisie une date possible.
            Jours : entre 1 et 31.
            Mois : entre 1 et 12.
            Année : entre 1900 et l'année actuelle moins seize.''')

def display_this_player_is_already_chosen():
    print('!! Le joueur choisi est déjà dans la liste des joueurs. !!')


def display_has_a_number():
    print('!! Les nombres ne sont pas autorisés. !!')
