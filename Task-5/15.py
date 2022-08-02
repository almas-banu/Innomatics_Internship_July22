# Validating Credit Card Numbers

import re
TEST = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$"
)

n = int(input())
for i in range(n):
    if TEST.search(input().strip()):
        print("Valid")
    else:
        print("Invalid")