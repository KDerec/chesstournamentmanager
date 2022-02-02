

class EmptyInputException(Exception):
    """Manage exception for empty input."""
    pass


class ModeOutOfRangeException(Exception):
    """Manage exception for out of range mode input."""
    pass


class NotPositiveIntegerException(Exception):
    """Manage exception for not positive integer input."""
    pass


class ImpossibleBirthdayDate(Exception):
    """Manage exception for impossible birthday date input."""
    pass


class WrongChosenPlayer(Exception):
    """Manage exception for already chosen player."""
    pass