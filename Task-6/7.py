# Array Mathematics

import numpy as np
nm = input().split()
n = int(nm[0])
m = int(nm[1])
a1 = [input().split() for i in range(n)]
b1 = [input().split() for j in range(n)]
a = np.array(a1,dtype=int)
b = np.array(b1,dtype=int)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.floor_divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))