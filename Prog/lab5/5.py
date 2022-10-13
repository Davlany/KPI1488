n = int(input())
value_list = []
for i in range(n+1):
    sqr_i = str(i**2)
    str_i = str(i)
    if sqr_i[-len(str_i):] == str_i:
        value_list.append(i)

for val in value_list:
    print(val)