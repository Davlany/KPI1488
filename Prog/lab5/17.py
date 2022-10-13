import math

N = int(input())

def is_default(n):
    n_list = [1,2,3,5,7]

    if n % 2 != 0 and n % 3 != 0 and n % 4 != 0 and n % 5 != 0 and n % 6 != 0 and n % 7 != 0 and n % 8 != 0 and n % 9 != 0 and n % math.sqrt(n) != 0:
        return True
    elif n in n_list: 
        return True
    else:
        return False

deff_list = []

for i in range(N):
    if is_default(i):
        deff_list.append(i)

deff_list2 = []

for num in deff_list:

    for j_num in deff_list:

        if j_num < num:

            if 2**j_num == num + 1:

                deff_list2.append(num)


print(deff_list2)