from views import userinput


def display_match_to_note(i, players):
    print(f'\nNotation match #{i} : '
            f'{players[0].first_name} {players[0].last_name} vs '
            f'{players[1].first_name} {players[1].last_name}')


def note_the_match(players):
    print(f'Résulat de {players[0].first_name} {players[0].last_name} '
            '(1 pour gagner, 0 perdu, 0.5 pour égalité) : ')

    return userinput.input_a_float()