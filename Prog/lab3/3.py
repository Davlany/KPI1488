print("Введіть х:")
x = float(input())

if x == -2:
    print("X не може дорівнювати -2, так як знаменник буде дорівнювати 0")
else:
    print("Введіть z:")
    z = float(input())

    if z == 0:
        print("Z не може бути нулем, бо z множник у знаменнику")
    else:
        y = (2 * x**2 + x - 5)/(x+2) + 1/math.tan(x/(2*z))
        print(y)