# Set .intersection() Operation

n = int(input())
nset = set(map(int,input().split()))
b = int(input())
bset = set(map(int,input().split()))

res = nset.intersection(bset)
stds = 0

for i in res:
    stds += 1
    
print(stds)