def count_digts(n):
	digits = 0
	while n > 0:
		n = n // 10
		digits += 1
	return digits 

def recurse_print_digits(n):
	d = 10**(count_digts(n)-1)
	if n % d == 0:
		print(n // d)       
	else:
		print(n // d, end = ' ')
		recurse_print_digits(n % d)

x = int(input())
print("Impressao em ordem: ", end = '')
recurse_print_digits(x)