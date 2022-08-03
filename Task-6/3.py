# Transpose and Flatten

import numpy as np

rc = input().split()
n = int(rc[0])
m = int(rc[1])
lst = [input().split() for i in range(n)]
my_arr = np.array(lst,int)
print(np.transpose(my_arr))
print(my_arr.flatten())