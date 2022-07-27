# Check Strict Superset
def strictsuperset():
    sub = set(map(int,input().split()))
    if sub.issubset(A):
        if len(A) == len(sub):
            lst.append(0)
        else:
            lst.append(1)
    else:
        lst.append(0)
    

A = set(map(int,input().split()))
n = int(input())
lst = []
for i in range(n):
    strictsuperset()
if all(lst) == 1:
    print('True')
else:
    print('False')
    
