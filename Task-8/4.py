# Normal Distribution 2

import math

mean, std = list(map(int,input().split(" ")))
gr1 = int(input())
pas = int(input())


nord = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))
hig80 = (1-nord(gr1))*100
pasmrk = (1-nord(pas))*100
fail = (nord(pas))*100

print(round(hig80,2))
print(round(pasmrk,2))
print(round(fail,2))