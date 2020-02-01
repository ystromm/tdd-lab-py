def to_int(str):
    lower = str.lower()
    if "i" == lower:
        return 1
    elif "ii" == lower:
        return 2
    elif "iii" == lower:
        return 3
    else:
        raise RomanNumberFormatException

class RomanNumberFormatException(Exception):
    pass
