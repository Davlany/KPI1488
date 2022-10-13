fib = [1,1]

while True:
    next_num = fib[-1] + fib[-2]
    if next_num <= 1000:
        fib.append(next_num)
    else: 
        break

print(fib)