import math
def calculate_inflation(rate, curr_amount, curr_year, tartget_year):
    if tartget_year > curr_year:
        return compound(rate, curr_amount, curr_year, tartget_year)
    else:
        return discount(rate, curr_amount, curr_year, tartget_year)

def compound(rate, curr_amount, curr_year, tartget_year):
    return curr_amount * ( (1 + rate) ** (tartget_year - curr_year) )

def discount(rate, curr_amount, curr_year, tartget_year):
    return curr_amount / ( (1 + rate) ** (curr_year - tartget_year) )