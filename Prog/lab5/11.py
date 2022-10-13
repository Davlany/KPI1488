n = input()
num_list = list(n)

if num_list[0] + num_list[2] == num_list[-1] + num_list[2]:
    print(f"{n} - це число-паліндром!")
else:
    print(f"{n} - це не число-паліндром :(")
