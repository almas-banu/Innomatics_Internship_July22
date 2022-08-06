# Binomial Distribution 2

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
    
def combi(n, r):
    return fact(n) / (fact(r) * fact(n-r))

def bina(x, n, p):
    return combi(n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int,input().split(" ")))

print(round(sum([bina(i,n,p/100) for i in range(3)]),3))

print(round(sum([bina(j,n,p/100) for j in range(2,(n+1))]),3))