# Set .difference() Operation

no_e = int(input())
english = set(map(int,input().split()))
no_f = int(input())
french = set(map(int,input().split()))

res = english.difference(french)
stds_e = 0

for i in res:
    stds_e += 1
    
print(stds_e)