# Group(),Groups() & Groupdict()

import re
s = input()
pattern = r'([a-z A-Z 0-9])\1'
n = re.search(pattern,s)
if n:
    print(n.groups()[0])
else:
    print(-1)