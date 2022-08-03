# Linear Algebra

import numpy

n = int(input())
lst = [input().split() for i in range(n)]
a_arr = numpy.array(lst,float)
print(numpy.linalg.det(a_arr).round(2))


