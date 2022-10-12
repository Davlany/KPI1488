def factorial_c(n):
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        res = 1
        for i in range(n):
            res *= i+1
        return res


print("ВВЕДІТЬ ЧИСЛО:")
n = int(input())
fact = factorial_c(n)
b = 0 

for x in range(n):
    if x*(x+1)*(x+2) == fact:
        print(f"Факторіал {n} = {fact}")
        print(f"x1: {x}\nx2: {x+1}\nx3: {x+2}")
        b = 1

if b == 0:
    print(f"Факторіал {n} = {fact}")
    print("Факторіал не має множників що відповідають умові")