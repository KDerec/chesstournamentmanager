"""Display player messages."""

from views import userinput


def validate_creation():
    """Display player creation validation and return user choice."""

    print('Validez-vous la création du joueur ? Si non, retour menu joueur.')
    
    return userinput.input_choice()


def change_player_rank():
    """Display ask player rank modification and return user choice."""

    print('Voulez-vous modifier le classement d\'un joueur ?')

    return userinput.input_choice()


def select_a_player_to_change_his_rank():
    """Display select a player and return user choice number."""

    print('Sélectionner un joueur pour modifier son classement.')

    return userinput.input_a_number()


def choice_new_rank():
    """Display enter a rank number and return number."""

    print('Entrer un nombre pour le nouveau classement : ')

    return userinput.input_a_number()