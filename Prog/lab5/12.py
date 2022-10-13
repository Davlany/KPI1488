num_list = []

for i in range(10, 100):
    str_i = str(i)
    if i / (int(str_i[0]) + int(str_i[1])) == 7:
        num_list.append(i)

print(num_list)