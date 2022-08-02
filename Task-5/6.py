# Regex Substitution

import re

n = int(input())
pattern = r"(?<= )(&&|\|\|)(?= )"
replacement = lambda x: "and" if x.group() == "&&" else "or"
for i in range(n):
    s = input()
    print(re.sub(pattern,replacement,s))