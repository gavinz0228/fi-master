from pandas.tseries.offsets import Day, BDay

def is_bday(x):
    return x == x + Day(1) - BDay(1)