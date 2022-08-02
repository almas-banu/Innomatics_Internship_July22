# Hex Color Code

import re
res = False

n = int(input())
for i in range(n):
    new = input()
    if '{' in new:
        res = True
    elif '}' in new:
        res = False
    elif res:
        for color in re.findall('#[0-9a-fA-F]{3,6}',new):
            print(color)