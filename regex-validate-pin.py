'''
Description: ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
'''
import re

def validate_pin(pin):
  '''
  Accepts PINs of 4 or 6 digits. 
  '''
  pattern = r"^\d{4}|\d{6}$"
  return re.fullmatch(pattern, pin) is not None
