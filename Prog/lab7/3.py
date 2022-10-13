#--------------1--------------#

#В первом технические проблемы)

#---------------2----------------#

def numbers_Kaplana(n):
	if n == 0:
		return 1
	else:
		num = 2*(2*n - 1)/(n + 1)*numbers_Kaplana(n-1)
		return num 

print(numbers_Kaplana(10))