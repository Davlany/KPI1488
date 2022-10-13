n = int(input())
m = int(input())

value_list = []

while n <= m:
    if n % 3 == 0 and n % 2 != 0:
        value_list.append(n)
    n += 1

print(value_list)