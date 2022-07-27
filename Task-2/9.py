# Symmetric Difference

m = input()
mset = set(map(int,input().split()))
n = input()
nset = set(map(int,input().split()))

result = sorted((mset-nset).union(nset-mset))

for i in result:
    print(i)