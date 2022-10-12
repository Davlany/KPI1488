N = int(input())

for i in range(N):
    sqr_num = str(i**2)
    str_i = str(i)
    if sqr_num[-len(str_i):] == list(str_i):
        print(i)
