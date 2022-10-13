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

while True:
    if len(deff_list) < 5:
        N += 1
        if is_default(N):
            deff_list.append(N)
    else:
        break
        
print(deff_list)