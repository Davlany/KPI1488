import math

c = int(input())
d = int(input())

value_list = []

while c < d:
    y = math.sin(c)*c - math.cos(c)
    value_list.append(y)
    c += 0.001

print(min(value_list))