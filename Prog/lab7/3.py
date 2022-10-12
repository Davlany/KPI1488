#--------------1--------------#

def factorial(n):
    if n == 0: 
        return 1
    elif n == 1:
        return 1

    return n * factorial(n-1)

def sin(x,n):
    res = ((-1)**n * x**(2*n+1))/factorial((2*n+1))
    if res != 0:
        n+=1
        return res + sin(x,n)
    else:
        return res

def cos(x,n):
    res = ((-1)**n * x**(2*n))/factorial((2*n))
    if res != 0:
        n+=1
        return res + cos(x,n)
    else:
        return res


def ctg(x):
    return cos(x,0)/sin(x,0)

try:
    x = float(input())
    z = float(input())
except:
    print("Невірне значення")

try:
    y = (2*x**2 + x - 5)/(x+2) + ctg(x/2*z)
except:
    print("Помилка, z не може бути нулем")
#---------------2----------------#

def numbers_Kaplana(n):
	if n == 0:
		return 1
	else:
		num = 2*(2*n - 1)/(n + 1)*numbers_Kaplana(n-1)
		return num 

print(numbers_Kaplana(10))