#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
arr = list(arr)
arr.sort(reverse = True)
winner = max(arr)
for i in arr:
    if i != winner:
        r = i
        break
print(r) 