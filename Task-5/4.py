# Re.findall() & Re.finditer()

import re
s = input()
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
pattern = r"(?<=[%s])([%s]{2,})[%s]"%(c,v,c)
lst = re.findall(pattern,s,flags=re.IGNORECASE)
if lst == []:
    print(-1)
else:
    for i in lst:
        print(i)