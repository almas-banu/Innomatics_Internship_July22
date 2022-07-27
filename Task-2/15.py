# Set .symmetric_difference() Operation
no_e = int(input())
english = set(map(int,input().split()))
no_f = int(input())
french = set(map(int,input().split()))

res = english.symmetric_difference(french)
stds_ef = 0

for i in res:
    stds_ef += 1
    
print(stds_ef)