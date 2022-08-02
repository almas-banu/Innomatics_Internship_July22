# Validating phone numbers

import re
def check(contact):
    pattern = r"[789]\d{9}$"
    if re.match(pattern,contact):
        return "YES"
    else:
        return "NO"
    
n = int(input())
for i in range(n):
    print(check(input()))