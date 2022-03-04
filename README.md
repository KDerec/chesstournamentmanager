<div id="top"></div>



<br />
<div align="center">
  <a href="https://github.com/KDerec/chesstournamentmanager.git">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Chess tournament manager</h3>
  <p align="center">
    Manage your tournaments, players, matchmaking,<br>scores and reports in one application. 
  </p>
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#technologies">Technologies</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#generate-html-reports-of-flake8-violations">Flake8 report</a></li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#tournament-creation-and-running-example">Tournament creation and running example</a></li>
        <li><a href="#player-creation-example">Player creation example</a></li>
        <li><a href="#report-display-example">Report display example</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



## About The Project

Chess tournament manager is an offline command line application with local database.  
With Chess tournament manager, you can :
* Create tournament with :
  * Name ;
  * location ;
  * date ;
  * time controller (bullet, blitz and rapide) ;
  * and description.
* Create players with :
  * Last name ;
  * first name ;
  * birthday ;
  * sexe ;
  * and rank.
* Play tournament and :
  * Select a number of round ;
  * select a number of player ;
  * select players from your local database ;
  * automatic player matchmaking according to swiss system ;
  * put a score for every match ;
  * play every rounds and display the standings !
* Display reporting of :
  * All actors ;
  * all tournaments ;
  * all players of a tournament ;
  * all rounds of a tournament ;
  * all matchs of a tournament.

Tournaments and players are all save in your local database.

<p align="right">(<a href="#top">back to top</a>)</p>




## Technologies

Python 3.9.6

<p align="right">(<a href="#top">back to top</a>)</p>

## Installation

1. Install Python at [https://www.python.org/](https://www.python.org/) ;
2. Clone the project in desired directory ;
   ```sh
   git clone https://github.com/KDerec/chesstournamentmanager.git
   ```
3. Change directory to project folder ;
   ```sh
   cd path/to/chesstournamentmanager
   ```
4. Create a virtual environnement *(More detail to [Creating a virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment))* ;
    * For Windows :
      ```sh
      python -m venv env
      ```
    * For Linux :
      ```sh
      python3 -m venv env
      ```
5. Activate the virtual environment ;
    * For Windows :
      ```sh
      .\env\Scripts\activate
      ```
    * For Linux :
      ```sh
      source env/bin/activate
      ```
6. Install package of requirements.txt ;
   ```sh
   pip install -r requirements.txt
   ```
7. Run main.py and let yourself be guided by the application.

<p align="right">(<a href="#top">back to top</a>)</p>



## Generate HTML reports of flake8 violations

1. Open a new terminal and change directory to project folder ;
   ```sh
   cd path/to/chesstournamentmanager
   ```
2. Run the below command ;
   ```sh
   flake8 --format=html --htmldir=flake-report
   ```
3. Change directory to flake-report folder ;
   ```sh
   cd ./flake-report
   ```
4. Open index.html.
   ```sh
   index.html
   ```
    * With Windows PowerShell :
      ```sh
      ./index.html
      ```
    * With Linux to display in the terminal :
      ```sh
      w3m -dump index.html
      ```

<p align="right">(<a href="#top">back to top</a>)</p>



## Usage

### Tournament creation and running example
![](https://github.com/KDerec/chesstournamentmanager/blob/master/images/tournament_example.gif)

### Player creation example
![](https://github.com/KDerec/chesstournamentmanager/blob/master/images/player_example.gif)

### Report display example
![](https://github.com/KDerec/chesstournamentmanager/blob/master/images/report_example.gif)

<p align="right">(<a href="#top">back to top</a>)</p>



## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

