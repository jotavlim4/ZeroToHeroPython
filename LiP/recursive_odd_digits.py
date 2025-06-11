def is_odd(n):
	if n % 2 == 1:
		return 1
	else:
		return 0

def recusive_odd_digits(n):
	if n // 10 == 0:
		return is_odd(n % 10)
	else: 
		return is_odd(n) + recusive_odd_digits(n // 10)

x = int(input())
print(f"{x} possui {recusive_odd_digits(x)} digitos impares")
