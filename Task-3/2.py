# Find Angle MBC

import math

ab = int(input())
bc = int(input())

res = math.atan(ab/bc)
res_d = math.degrees(res)
print(round(res_d),chr(176),sep='')
