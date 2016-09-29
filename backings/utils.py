from decimal import Decimal

# Helper functions for credit cards, numbers, prices
def digits_of(number):
    return list(map(int, str(number)))

def luhn_checksum(card_number):
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(digits_of(2 * digit))
    return total % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

def card_is_correct(card):
    # Todo: Removed isdigit, where should this go now
    try:
        if len(str(card)) < 20 and is_luhn_valid(card):
            return True
        return False
    except ValueError:
        return False

def name_is_correct(name):
    if name.isalnum() and 4 <= len(name) <= 20:
        return True
    return False

def remove_dollar_sign(price):
    if type(price) == str:
        if price[0] == '$':
            price = price[1:].replace(",", "")
        return price

def price_is_correct(price):
    # Todo: Work on this
    try:
        float(price)
        return True
    except:
        return False

def convert_to_decimal(str):
    num = Decimal(str)
    return round(num, 2)
