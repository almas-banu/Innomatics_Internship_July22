#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

lst = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
lst1 = [[a,b,c] if a+b+c == n else [] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
i = 0
while i < len(lst1):
    if lst1[i] in lst:
        lst.remove(lst1[i])
    else:
        pass
    i+=1
print(lst)