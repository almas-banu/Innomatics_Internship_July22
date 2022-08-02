# Validating and Parsing Email Addresses

import re
n = int(input())
for i in range(n):
    o, p = input().split(' ')
    pattern = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', p)
    if pattern:
        print(o,p)