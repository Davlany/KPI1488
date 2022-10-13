import math

c = float(input())
d = float(input())

res_list = []

while c <= d:
    y = math.sin(c*c)*c + math.cos(c)
    res_list.append(y)
    c+=0.001

print(min(res_list))