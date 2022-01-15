"""Définit un joueur."""


class Player:
    def __init__(self, name, surname, birthday, sexe, rank):
        """Initialise un joueur."""
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.sexe = sexe
        self.rank = rank