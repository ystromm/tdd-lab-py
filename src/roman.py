def to_int(roman_str):
    
# shirt = 'white' if game_type == 'home' else 'green'
  if isRomanNumber(roman_str):
    number = 2 if roman_str.upper() == 'II' else 1
    return number
  else:
    raise NotARomanNumber()

def isRomanNumber(roman_str): 
  return True if (roman_str.upper() == 'I' or roman_str.upper() == 'II') else False

class NotARomanNumber(Exception):
    pass
