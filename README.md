# Chess tournament manager
***
This app is an offline chess tournament manager.
The user can run tournament, add players to a database and view reports.
## Technologies
Python 3.9.6
## Installation
***
* Install Python (https://www.python.org/),
* clone the project in desired directory,

    > git clone https://github.com/KDerec/chesstournamentmanager.git

* change directory to project folder,

    > cd chesstournamentmanager

* Create a virtual environnement,
    * For Windows :

    > python -m venv env

    * For Linux :

    > python3 -m venv env

More detail to [Creating a virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

* activate the virtual environment,
    * For Windows :

    > .\env\Scripts\activate

    * For Linux :

    > source env/bin/activate

* install package in requirements.txt,

    > pip install -r requirements.txt

* run main.py and let yourself be guided by the application.
## Usage example
***
The example below show the creation and the running of a tournament :

![](https://github.com/KDerec/chesstournamentmanager/blob/master/usage_example.gif)
## Generate HTML reports of flake8 violations
***
* Open a new terminal and change directory to project folder,

    > cd path/to/chesstournamentmanager

* run the below command,

    > flake8 --format=html --htmldir=flake-report

* change directory to flake-report folder,

    > cd ./flake-report

* open index.html

    > index.html

    * With Windows PowerShell :

    > ./index.html

    * With Linux to display in terminal :

    > w3m -dump index.html

## TODO 
***
* Vérifier que l'application fonctionne sous mac.
