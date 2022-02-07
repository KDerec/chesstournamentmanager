from views import systemview


def exit_application():
    choice = systemview.display_exit_message()
    if choice.upper() == 'Q':
        exit()


def choice_verification(choice):
    if choice.upper() == 'O':
        return True