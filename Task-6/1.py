# Arrays

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    array_numpy = numpy.array(arr,float)
    return array_numpy[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
