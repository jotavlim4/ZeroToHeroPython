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

print(sophie_german(3))
