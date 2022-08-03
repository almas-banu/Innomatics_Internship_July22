# Polynomials

import numpy

arr = numpy.array(input().split(),float)
x = int(input())
print(float((numpy.polyval(arr,x))))

