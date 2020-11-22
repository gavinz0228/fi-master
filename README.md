# fi-master
A python library for Fixed-income data and valuation.

## Usage:
```python
from fimaster.data_api import get_yield_curve, get_yield_curve_by_dates
```
get yield curve data for a specific date, returns a pandas dataframe
```python
data = get_yield_curve(2020, 11, 2)
```
get daily yield curve data for a month(just not to specifiy a day)
```python
data = get_yield_curve(2020, 11)
```
for the whole year
```python
data = get_yield_curve(2020)
```

get daily yield curve for dates specified:
```python
get_yield_curve_by_dates
```