n = input()
num_list = list(n)

if int(num_list[0]) + int(num_list[1]) + int(num_list[2]) == int(num_list[3]) + int(num_list[4]) + int(num_list[5]):
    print(f"{n} - це щасливе число! Слава Україні!")
else:
    print(f"{n} - це не щасливе число :(")