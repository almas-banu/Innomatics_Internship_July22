# Set .discard(),.remove() & .pop()

n = int(input())
s = set(map(int, input().split()))

no_commands = int(input())

for i  in range(no_commands):
    cmd = input().split()
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "remove":
        s.remove(int(cmd[1]))
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))
    else:
        print("No such operation by set")
    
sum = 0
for i in s:
    sum += i
    
print(sum)