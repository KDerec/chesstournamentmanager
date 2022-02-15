# Chess tournament manager
***
Cette application est un gestionnaire de tournoi d'échec hors ligne.
L'utilisateur peux déclencher le déroulement d'un tournoi, ajouter des joueurs dans une base de donnée et afficher/exporter des rapports des tournois.
## Installation
***
* Install Python (https://www.python.org/), 
* run a virtual environnement in the current directory of the script,
> python -m venv env
* install package in requirements.txt,
> pip install -r /path/to/requirements.txt
* run main.py and let yourself be guided by the application.
## Usage example
***
L'exemple ci-dessous montre la création et le déroulement d'un tournoi.
La création des joueurs est réalisée de manière automatique et ceci ne sera plus le cas dans la version finale.
![](https://github.com/KDerec/chesstournamentmanager/blob/master/usage_example.gif)
## TODO 
***
* Vérifier que l'application fonctionne sous mac et linux,

Ajouter la fonctionnalité d'affichage de rapport :
* Liste de tous les joueurs d'un tournoi :
    * par ordre alphabétique ;
    * par classement.
* Liste de tous les tours d'un tournoi.
* Liste de tous les matchs d'un tournoi.

* Utiliser flake8 pout le peluchage du code,
_Pour effectuer le peluchage du code, veuillez utiliser flake8 avec l'option de longueur de ligne maximale fixée à 119. Nous aimerions également voir un rapport généré par flake8-html dans le repository, sous un répertoire appelé "flake8_rapport", qui n'affiche aucune erreur et nous assurera que votre code est conforme aux directives PEP 8._

* Instruction pour générer un rapport flake8.