# Eye and Identity

import numpy
numpy.set_printoptions(legacy='1.13')

nm = input().split()
n = int(nm[0])
m = int(nm[1])
print(numpy.eye(n,m))