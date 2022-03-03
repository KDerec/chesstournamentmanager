"""Display player messages."""


from views import userinput


def validate_creation():
    """Display player creation validation and return user choice."""
    print("Validez-vous la création du joueur ? Si non, retour menu joueur.")

    return userinput.input_choice()


def display_player_summary(self):
    """Display player attributs."""
    print(
        f"""Récapitulatif :
    Nom: {self.last_name}
    Prénom: {self.first_name}
    Date de naissance: {self.birthday}
    Sexe: {self.sexe}
    Classement: {self.rank}"""
    )


def change_player_rank():
    """Display ask player rank modification and return user choice."""
    print("Voulez-vous modifier le classement d'un joueur ?")

    return userinput.input_choice()


def select_a_player_to_change_his_rank():
    """Display select a player and return user choice number."""
    print("Sélectionner un joueur pour modifier son classement.")

    return userinput.input_a_number()


def choice_new_rank():
    """Display enter a rank number and return number."""
    print("Entrer un nombre pour le nouveau classement : ")

    return userinput.input_a_number()


def display_player_rank_is_update(self):
    """Display player last and first name with new rank value."""
    print(f"Le classement de {self.last_name} {self.first_name} est mis à jour ({self.rank}).")


def display_added_player_message(self):
    """Display added player message."""
    print(f"{self.last_name} {self.first_name} est ajouté.\n")
