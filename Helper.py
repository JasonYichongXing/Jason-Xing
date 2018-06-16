import calendar

def lastbusinessday(year, month):
    '''
   return the last business day of the month. 
    '''
    
    _, day = calendar.monthrange(year, month)
    weekday = calendar.weekday(year, month, day)
    if weekday == 6:
        return day - 2
    elif weekday == 5:
        return day - 1
    return day


# or using pandas function:
import pandas as pd

pd.date_range('2018', periods= 12, freq='CBM') # Last Business Day of every month
pd.date_range('2018', periods= 12, freq='BMS') # First Business Day of every month
