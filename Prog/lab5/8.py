fib = [1,1]
m = int(input())
res = 0
if m > 1:
    while True:
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)
        if next_num > m:
            res = next_num
            break
else:
    print("m повинно бути більше за 1")

print(res)