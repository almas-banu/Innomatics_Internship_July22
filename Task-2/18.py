# Check Subset

def subsetfun():
    x = int(input())
    A = set(map(int,input().split()))
    y = int(input())
    B = set(map(int,input().split()))
    lst = []
    for i in A:
        if i in B:
            lst.append(i)
    lst = set(lst)
    if lst == A:
        print("True")
    else:
        print("False")
        
test_case = int(input())
for test in range(test_case):
    subsetfun()