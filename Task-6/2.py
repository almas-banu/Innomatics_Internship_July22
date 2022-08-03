# Shape and Reshape

import numpy

arr = input().strip().split(' ')
new_array = numpy.array(arr,int)
print(numpy.reshape(new_array,(3,3)))

