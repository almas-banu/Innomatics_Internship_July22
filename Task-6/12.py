# Dot and Cross

import numpy

n = int(input())
a_lst = [input().split() for i in range(n)]
b_lst = [input().split() for j in range(n)]
a = numpy.array(a_lst,int)
b = numpy.array(b_lst,int)
print(numpy.dot(a,b))