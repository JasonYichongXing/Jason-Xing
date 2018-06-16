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


