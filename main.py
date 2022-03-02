from controllers import menucontroller
from controllers import tournamentcontroller


def main():
    tournamentcontroller.check_if_a_tournament_is_not_over()
    menucontroller.run()


if __name__ == "__main__":
    main()
