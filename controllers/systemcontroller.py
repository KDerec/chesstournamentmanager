from views import systemview


def exit_application():
    choice = systemview.display_exit_message()
    if choice.upper() == 'Q':
        exit()