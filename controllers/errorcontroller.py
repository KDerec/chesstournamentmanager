

class EmptyInputException(Exception):
    """Manage exception for empty input."""
    pass


class ModeOutOfRangeException(Exception):
    """Manage exception for out of range mode input."""
    pass


class NotPositiveIntegerException(Exception):
    """Manage exception for not positive integer input."""
    pass


class ImpossibleBirthdayDateException(Exception):
    """Manage exception for impossible birthday date input."""
    pass


class WrongChosenPlayerException(Exception):
    """Manage exception for already chosen player."""
    pass


class HasNumberException(Exception):
    """Manage exception for number in a list of string"""
    pass