num_list = []
n = int(input())


for i in range(1,n+1):
    num_list.append(i)

print(num_list)
sum = 0

while True:
    if len(num_list) >= 2:
        sum += num_list[0]/num_list[1]
        del num_list[0]
        del num_list[0]
    else:
        break

print(sum)