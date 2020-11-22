import sys
from os import path
from datetime import date, datetime
sys.path.append(path.join(path.dirname(__file__), '..'))

from fimaster.utils import get, is_bday
from fimaster.data_api import get_yield_curve, get_yield_curve_by_dates

def test_get():
    print("get xml from us treasury gov")
    url = "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/XmlView.aspx?data=yield"
    assert len(get(url)) > 0

def test_bus_day_check():
    assert is_bday(datetime(2020, 11, 1)) == False
    assert is_bday(datetime(2020, 11, 2)) == True

def test_get_one_day():
    print('get a day')
    data = get_yield_curve(2020, 11, 2)
    assert len(data) > 0

def test_get_month():
    print('get a month')
    data = get_yield_curve(2020, 11)
    assert len(data) > 0

def test_get_year():
    print('get curr year')
    data = get_yield_curve(2020)
    assert len(data) > 0

def test_get_multiple_dates():
    print('get multiple dates')
    data = get_yield_curve_by_dates([datetime(2020, 7, 2), datetime(2020, 11, 2), datetime(2020, 10, 2),datetime(2020, 9, 2)])
    assert len(data) > 0


if __name__ == '__main__':
    test_get()
