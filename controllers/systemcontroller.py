from views.message import menumessage


def exit_application():
    choice = menumessage.display_exit_message()
    if choice.upper() == 'Q':
        exit()