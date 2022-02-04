from views import userinput


def validate_creation():
    print('Validez-vous la création du joueur ? Si non, retour menu joueur.')
    
    return userinput.input_choice()


def change_player_rank():
    print('Voulez-vous modifier le classement d\'un joueur ?')

    return userinput.input_choice()


def select_a_player_to_change_his_rank():
    print('Sélectionner un joueur pour modifier son classement.')

    return userinput.input_a_number()


def choice_new_rank():
    print('Entrer un nombre pour le nouveau classement : ')

    return userinput.input_a_number()