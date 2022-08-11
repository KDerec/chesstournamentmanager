"""Display match messages."""


from views import userinput


def display_match_to_note(i, players):
    """Display match to note."""
    print(
        f"\nNotation match #{i} : "
        f"{players[0].first_name} {players[0].last_name} vs "
        f"{players[1].first_name} {players[1].last_name}"
    )


def note_the_match(self):
    """Display player name and surname and return his result."""
    print(
        f"Résulat de {self[0].first_name} {self[0].last_name} "
        "(1 pour gagner, 0 perdu, 0.5 pour égalité) : "
    )

    return userinput.input_a_float()


def validate_match_result():
    """Display message and return user input."""
    print("Validez-vous les scores ?")

    return userinput.input_choice()
