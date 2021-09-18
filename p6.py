# wapf to find the sum of digits 

def sod(num):
	sum = 0
	while num > 0:
		digit = num % 10 
		sum =  sum + digit
		num =  num // 10
	return sum
num = int(input(" enter a number "))
ans = sod(num)
print(" sum = ", ans)