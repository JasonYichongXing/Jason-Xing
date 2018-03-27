import numpy
import pandas as pd

#import from xls
DS = pd.read_excel('M:/Desktop/Book3.xls', name = 'sheet1', index_col = 0). #datasource including row index and col index
DS = DS.T
Dvalue = DS.values. # impact is saved into Dvalue as float

Tenor_Pair = list(DS[1:1])
Expiry = list(DS.index)

x_ind, y_ind = numpy.where(Dvalue == Dvalue.max())
print('The location of maximpact is (%s,%s), which is %.2f. ' %(Expiry[x_ind[0]], Tenor_Pair[y_ind[0]], Dvalue[x_ind, y_ind])) 

