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

if is_default(N):
    deff_list.append(N)

deff_list2 = []

for dn in deff_list:
    if N % dn == 0:
        deff_list2.append(dn)

print(deff_list2)