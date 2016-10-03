import re

from decimal import Decimal
from painter import paint
from settings.constants import ERROR_MSG

# Helper functions for syntax and formatting

def correct_char_count(str, min, max):
    chars = len(str)
    if min <= chars <= max:
        return True
    else:
        return False


def card_is_correct(card):
    try:
        if len(str(card)) < 20 and is_luhn_valid(card):
            return True
        return False
    except ValueError:
        return False


def convert_to_decimal(str):
    num = Decimal(str)
    return round(num, 2)


def correct_char_count(str, min, max):
    chars = len(str)
    if min <= chars <= max:
        return True
    else:
        return False

# Confirm there are enough parameters
def correct_amount_args(args, expected_args):
    length = len(args)
    if length != expected_args:
        print paint.red(u'{}\nPlease make sure you\'re using the right number of variables.').format(ERROR_MSG)
        return False
    else:
        return True


def is_alphanumeric(str):
    if re.match("^[A-Za-z0-9_-]*$", str):
        return True
    else:
        return False


def is_numeric(str):
    """See if string is numeric."""
    try:
        float(str)
    except ValueError:
        return False
    return True


def name_is_correct(name):
    if name.isalnum() and 4 <= len(name) <= 20:
        return True
    return False


def remove_dollar_sign(price):
    if type(price) == str:
        if price[0] == '$':
            price = price[1:].replace(",", "")
        return price
