"""Displays error messages."""


def display_wrong_choice_message():
    """Display message the user input an unauthorized number."""

    print('!! Vous n\'avez pas choisi un chiffre valide. !!')


def display_not_an_integer_message():
    """Display message the user not input an integer."""

    print('!! Vous n\'avez pas choisi un nombre entier. !!')


def display_not_an_integer_or_float_number():
    """Display message the user not input an float."""

    print('!! Vous n\'avez pas choisi un nombre entier ou à virgule. !!')


def display_its_blank_message():
    """Display message the user input is blank."""

    print('!! Vous n\'avez pas saisie de texte. !!')


def display_not_in_selection_range():
    """Display message the user input out of range number."""

    print('!! Vous n\'avez pas saisie un numéro de la sélection valide. !!')


def display_not_positive_integer():
    """Display message the user input not an positive number."""

    print('!! Vous n\'avez pas saisie un entier positif. !!')


def display_not_possible_birthday_date():
    """Display message the user input an impossible date."""

    print('''Vous n\'avez pas saisie une date possible.
            Jours : entre 1 et 31.
            Mois : entre 1 et 12.
            Année : entre 1900 et l'année actuelle moins seize.''')

def display_this_player_is_already_chosen():
    """Display message the user chosen player is already in player list."""

    print('!! Le joueur choisi est déjà dans la liste des joueurs. !!')


def display_has_a_number():
    """Display message the user input a number."""

    print('!! Les nombres ne sont pas autorisés. !!')


def display_not_an_even_number():
    """Display message the user not input an even number."""

    print('!! Vous n\'avez pas saisie un nombre pair. !!')


def display_you_selected_too_much_player():
    """Display message the user selected too much player."""

    print('!! Vous avez saisie plus de joueur que de joueur dans la base de donnée. !!')