#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 09:06:36 2018

@author: xingyichong
"""
import numpy

#input:
Rows = 100
Cols = 200      
R = numpy.random.rand(Rows,Cols)*100.  # eq. numpy.random.random((Rows,Cols))

row_index = ['E{}'.format(i) for i in range(Rows)]  
col_index = ['T{}'.format(i) for i in range(Cols)]

#indexing:
xind, yind = numpy.where(R == R.max())

print('The location of maxium in matrix is (%d, %d), which is %.2f. ' %(xind, yind, R[xind,yind]))


Tenor_pair_summary = R.sum(axis = 0)  #by col, as the header or col_index is Tenor_pair

Tenor_pair_maxindex = numpy.where(Tenor_pair_summary == Tenor_pair_summary.max())
print('The max tenorpair is %s, which is %.2f ' %(col_index[Tenor_pair_maxindex[0][0]],Tenor_pair_summary[Tenor_pair_maxindex]))

print(R[:,Tenor_pair_maxindex])  #print out the col with max sum.

exp_maxindex = numpy.where(R[:,Tenor_pair_maxindex] == R[:,Tenor_pair_maxindex].max())
print('The max expiry is %s' % row_index[exp_maxindex[0][0]])
