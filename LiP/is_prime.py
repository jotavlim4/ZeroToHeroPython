import math

def is_prime(n):
	if n <= 1:
		return False
	else:
		for i in range(2, int(math.sqrt(n)) + 1):
			if n % i == 0:
				return False
	return True


if __name__ == '__main__':
	number = int(input())
	print(is_prime(number))