import math

def is_prime(n):
	if n <= 1:
		return False
	else:
		for i in range(2, int(math.sqrt(n)) + 1):
			if n % i == 0:
				return False
	return True

def sophie_german(n):
	if is_prime(n) and is_prime(2*n + 1):
		return True
	return False

def sophie_german_intervalo(a = 10, b = 150):
	for i in range(a, b + 1):
		if sophie_german(i):
			print(i, end = ' ')
	print()

if __name__ == '__main__':
	sophie_german_intervalo(1, 10000)