def to_int(str):
    if str == "I":
        return 1
    elif str == "II":
        return 2
    else:
        raise RomanNumberFormatException

class RomanNumberFormatException(Exception):
    pass
