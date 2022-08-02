# Re.start() & Re.end()

import re
s = input()
k = input()
pattern = re.compile(k)
l = pattern.search(s)
if not l:
    print("(-1, -1)")
else:
    while l:
        print("({0}, {1})".format(l.start(),l.end()-1))
        l = pattern.search(s,l.start()+1)