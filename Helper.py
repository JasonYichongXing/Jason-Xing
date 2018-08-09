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
# 1. list file names and last modified time
# 2. Rename multiple files
############################### 
from os import listdir, rename
from os.path import isfile, join, getmtime
from datetime import datetime

def listfile(path):
    for f in listdir(path):
        if isfile(join(path,f)):
            ftime = getmtime(join(path, f))
            ftime = datetime.fromtimestamp(ftime).strftime('%y-%m-%d %H:%M:%S')
        yield f, ftime
        

        
        
def str_SplitCap(name):
    for word in name:
        if word.lower() not in ['of', 'for', 'in', 'and', 'to', 'at']:
            word = word.capitalize()
        else:
            word = word.lower()
        yield word        
        
def filerename(path, filetype='pdf'):
    for nfile in listfile(path):
        bookname = nfile.split('.')[0]
        ren = ' '.join(str_SplitCap(bookname.split(' ')))
        rename(path+nfile, path+ren+'.'+filetype) 
        
        
###############################
# couple recursive solutions:
# 1. Combination. nCr
# 2. Catalan number
############################### 
from functools import lru_cache

@lru_cache(maxsize = 1000)
def comb(n, r):
    if n < r:
        return 0
    if n == r or r == 0:
        return 1
    else:
        return comb(n-1, r) + comb(n-1, r-1)
    
# can also use Scipy function:
# from scipy.special import comb
# comb(n, r)



def catalan(n):
    if n == 0:
        return 1
    
    cat = 0
    for i in range(n):
        cat += catalan(i) * catalan(n-i-1)
    return cat

###############################
# Transfer between 2D Grid <-> List
###############################
# By Default, i.e, Vol Surface, the column name of rawtable is 'Tenor' while the raw name is 'Expiry'
#       T1Y   T2Y   T3Y   T4Y   T5Y   T7Y
# Vega                                    
# 1Y    0.76  0.25  0.77  0.83  0.91  0.03
# 2Y    0.91  0.14  0.13  0.24  0.59  0.01
# 3Y    0.65  0.86  0.55  0.52  0.53  0.79
# 4Y    0.92  0.68  0.17  0.03  0.43  0.50
#
# unpivot is to transfer grid to list.
# repivot is to tramsfer list back to grid.

def unpivot(rawtable, row_name='Expiry', col_name='Tenor', val_name='Impact'):
    table = rawtable.copy()
    table[row_name] = table.index
    return pd.melt(
            table, id_vars=row_name, var_name=col_name, value_name=val_name)


def repivot(list, val='Impact', ind='Expiry', col='Tenor'):
    return list.pivot(values=val, index=ind, columns=col)



