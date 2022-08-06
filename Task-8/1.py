# Binomial Distribution 1

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
    
def combi(n, r):
    return fact(n) / (fact(r) * fact(n-r))

def bina(x, n, p):
    return combi(n, x) * p**x * (1-p)**(n-x)

b, g = list(map(float, input().split(" ")))
russ = b / g
print(round(sum([bina(i, 6, russ / (1 + russ)) for i in range(3, 7)]), 3))
