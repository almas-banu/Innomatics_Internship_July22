# The Central Limit Theorem 2

import math

def nord(mean,std,x):
    z = (x - mean)/std
    return 0.5*(1 + math.erf(z/math.sqrt(2)))

x = float(input())
n = float(input())
mean = float(input())
std = float(input())

mean_new = n*mean
std_new = math.sqrt(n)*std

print(round(nord(mean_new,std_new,x),4))