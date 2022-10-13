n = int(input())

fibonachi = [1,1]

for i in range(n+1):
    fibonachi.append(fibonachi[-1] + fibonachi[-2])

print(fibonachi)