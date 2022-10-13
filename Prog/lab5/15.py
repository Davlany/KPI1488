import math

N = int(input())

def is_default(n):
    n_list = [1,3,5,7]

    if n % 2 != 0 and n % 3 != 0 and n % 4 != 0 and n % 5 != 0 and n % 6 != 0 and n % 7 != 0 and n % 8 != 0 and n % 9 != 0 and n % math.sqrt(n) != 0:
        return True
    elif n in n_list: 
        return True
    else:
        return False

deff_list = []
deff_list2 = []

for i in range(N):
    if is_default(i):
        deff_list.append(i)

for dn in deff_list:
    if is_default(dn + 6) and dn + 6 < N:
        deff_list2.append((dn,dn+6))

print(deff_list2)