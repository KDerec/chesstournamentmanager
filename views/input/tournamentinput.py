"""Base view"""


from models.tournament import Tournament


class InputTournament(Tournament):
    def __init__(self, name=False, location=False, date=False, 
                time_controller=False, number_of_rounds=False,
                description=False, duration = False):
        super().__init__(name, location, date, time_controller, 
                        number_of_rounds, description)
        self.duration = duration

    def input_name(self):
        self.name = str(input('Quelle est le nom du tournoi ? : '))

    def input_location(self):
        self.location = str(input('Où ce déroule le tournoi ? : '))
    
    def input_mode(self):
        print(f'Voici les modes de gestion de temps : {self.mode}.')
        return int(input(f'Quelle mode choisissez-vous ? '
                            '(Tapez un chiffre) : '))

    def input_duration(self):
        self.duration = int(input('Combien de jour le tournoi '
                                    'vas-t-il durer ? : '))

    def input_number_of_rounds(self):
        print('Le nombre de tour par défaut est de 4. '
                'Souhaitez-vous le modifier ?')
        choice = self.input_choice()
        if choice.upper() == 'O':
            self.number_of_rounds = int(input('Combien de tour ? : '))
        else:
            self.number_of_rounds = 4

    def input_description(self):
        print('Ajouter une description ?')
        choice = self.input_choice()
        if choice.upper() == 'O':
            self.description = input('Votre description : ')
        else:
            self.description = ''

    def input_choice(self):
        return input('Oui = o : ')

    def display_summary(self):
        print(f'''Récapitulatif :
        Nom du tournoi: {self.name}
        Localisation: {self.location}
        Mode de jeux: {self.time_controller}
        Durée du tournoi: {self.duration} jours
        Nombre de tour: {self.number_of_rounds}
        Description: {self.description}''')

    def validate_creation(self):
        print('Validez-vous la création du tournoi ? '
                'Si non, retour menu tournoi.')
        choice = self.input_choice()
        if choice.upper() == 'O':
            return True
        else:
            return False

