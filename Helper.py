import calendar
import numpy as np
import pandas as pd

###############################
# Last Business Day
###############################

def lastbusinessday(year, month):
    """ return the last business day of the month """
    _, day = calendar.monthrange(year, month)
    weekday = calendar.weekday(year, month, day)
    if weekday == 6:
        return day - 2
    elif weekday == 5:
        return day - 1
    return day

# or using pandas function:
pd.date_range('2018', periods= 12, freq='CBM') # Last Business Day of every month
pd.date_range('2018', periods= 12, freq='BMS') # First Business Day of every month


###############################
# Return
###############################
# To calculate the simple returns and log returns of a DataFrame
# Here, we skip the NA check to speed up the process
# The Pandas BIF pct_change() has the fillna and freq options, which will be very slow if our data dimension is a bit large.

def simplereturn(data):
    rs = data.div(data.shift(1)) - 1
    rs.iloc[0] = 0
    return rs

def logreturn(data):
    rs = np.log(data.div(data.shift(1)))
    rs.iloc[0] = 0
    return rs

def simple2log(ret):
    """ transfer simple returns to log returns."""
    return np.log(ret + 1)

def pct(data):
    """ transfer absolute price to percentage start with 0."""
    if (data.iloc[0] == 0).any():
        raise ValueError('ERROR: one or more elements of the first row are zero.')
    return data/data.iloc[0] - 1
        
        
###############################
# list file names and last modified time
############################### 
from os import listdir
from os.path import isfile, join, getmtime
from datetime import datetime

def listfile(path):
    for f in listdir(path):
        if isfile(join(path,f)):
            ftime = getmtime(join(path, f))
            ftime = datetime.fromtimestamp(ftime).strftime('%y-%m-%d %H:%M:%S')
        yield f, ftime
        
        
