# Multiple Linear Regression

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

m,n = [int(i) for i in input().strip().split(' ')]
x = []
y = []

for j in range(n):
    new = input().strip().split(' ')
    x.append(new[:m])
    y.append(new[m:])

q = int(input().strip())
x_new = []

for k in range(q):
    x_new.append(input().strip().split(' '))

x = np.array(x,float)
y = np.array(y,float)
x_new = np.array(x_new,float)


x_r = x-np.mean(x,axis=0)
y_r = y-np.mean(y)

b = np.dot(np.linalg.inv(np.dot(x_r.T,x_r)),np.dot(x_r.T,y_r))


x_new_r = x_new-np.mean(x,axis=0)
y_new_r = np.dot(x_new_r,b)
y_new = y_new_r + np.mean(y)


for i in y_new:
    print(round(float(i),2))