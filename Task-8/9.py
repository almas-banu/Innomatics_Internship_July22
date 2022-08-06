# Least Square Regression Line 

n = 5
xy = [map(int,input().split()) for i in range(n)]

sx, sy, sx2, sxy = map(sum, zip(*[(i, j, i**2, i * j) for i, j in xy]))

b = (n*sxy - sx*sy)/(n*sx2 - sx**2)

a = (sy/n) - b*(sx/n)

print(round(a+(b*80),3))

