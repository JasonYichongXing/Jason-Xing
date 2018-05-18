import numpy
import pandas as pd

DS = pd.read_excel('Book3.xls', name = 'sheet1', index_col = 0). #datasource including row index and col index
DS = DS.T
Dvalue = DS.values. # impact is saved into Dvalue as float

Tenor_Pair = list(DS[1:1])
Expiry = list(DS.index)

x_index, y_index = numpy.where(Dvalue == Dvalue.max())
print('The location of maximpact is (%s,%s), which is %.2f. ' %(Expiry[x_index[0]], Tenor_Pair[y_index[0]], Dvalue[x_index, y_ind])) 

