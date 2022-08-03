# Min and Max

import numpy

nm = input().split()
n = int(nm[0])
m = int(nm[1])
lst = [input().split() for i in range(n)]
my_arr = numpy.array(lst,int)
min_arr = numpy.min(my_arr,axis = 1)
print(numpy.max(min_arr))
