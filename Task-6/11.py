# Mean,Var,and Std

import numpy


nm = input().split()
n = int(nm[0])
m = int(nm[1])
lst = [input().split() for i in range(n)]
my_arr = numpy.array(lst,int)
print(numpy.mean(my_arr, axis = 1))
print(numpy.var(my_arr, axis = 0))
print(numpy.std(my_arr, axis = None).round(11))