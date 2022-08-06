# Normal Distribution 1

import math

mean, std = list(map(int,input().split(" ")))
q1 = float(input())
q2a, q2b = list(map(int,input().split(" ")))

def integration(fun,b,n=10000):
    st = 1/n
    if(b<0):
        st = -st
    n=int(abs(b)*n)
    a=0.0
    sq=0.0
    for i in range(0,n):
        sq += st * fun(a)
        a+=st
    return abs(sq)

erf = lambda b : (2*math.pi**(-0.5)) * integration(lambda x: math.exp(-x**2),b)
phi = lambda b : (1 + erf( (b-mean) / (std * 2**0.5) ))/2
q1ans = phi(0.0) - phi(q1)
q2ans = phi(q2b) - phi(q2a)

print(round(q1ans,3))
print(round(q2ans,3))


