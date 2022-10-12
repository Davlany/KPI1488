import math

c = float(input())
d = float(input())
res = []

while c < d:
    y = math.sin(c)*c
    res.append(y)
    c+=0.001

min_value = min(res)
print(min_value)