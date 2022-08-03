# Sum and Prod

import numpy

nm = input().split()
n = int(nm[0])
m = int(nm[1])
lst = [input().split() for i in range(n)]
my_arr = numpy.array(lst,int)
sum_arr = numpy.sum(my_arr,axis = 0)
print(numpy.prod(sum_arr)) 

