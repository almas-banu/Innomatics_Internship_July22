# Concatenate

import numpy

npm = input().split()
n = int(npm[0]) 
p = int(npm[2])
m = int(npm[1])
l1 = [input().split() for i in range(n)]
np_arr = numpy.array(l1,int)
l2 = [input().split() for j in range(m)]
mp_arr = numpy.array(l2,int)
print(numpy.concatenate((np_arr,mp_arr),axis = 0))

