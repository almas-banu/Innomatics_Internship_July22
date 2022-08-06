# The Central Limit Theorem 1


import math

def nord(mean,std,x):
    z = (x - mean)/std
    return 0.5*(1 + math.erf(z/math.sqrt(2)))

x = int(input())
n = int(input())
mean = int(input())
std = int(input())

mean_new = n*mean
std_new = math.sqrt(n)*std

print(round(nord(mean_new,std_new,x),4))