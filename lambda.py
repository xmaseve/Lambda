# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 20:32:29 2016

@author: YI
"""
#the usage of lambda
list1=[1,2,6,4]
list2=[3,4,2,6]

data=zip(list1,list2)

#data sorted by the first element of the tuple
data.sort()
#output: [(1, 3), (2, 4), (4, 6), (6, 2)]

#sort by the second element
data.sort(key=lambda x: x[1])
#output: [(6, 2), (1, 3), (2, 4), (4, 6)]

#parallel sorting
data.sort()
list1, list2 = map(lambda x: list(x), zip(*data))

