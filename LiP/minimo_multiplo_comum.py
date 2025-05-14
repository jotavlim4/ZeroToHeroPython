import math

def is_prime(n):
	'''
	recebe um número inteiro positivo
	e retorna True se for primo ou 
	False se não for primo.	
	'''
	if n <= 1:
		return False
	else:
		for i in range(2, int(math.sqrt(n)) + 1):
			if n % i == 0:
				return False
	return True

def mmc(n1, n2):
	'''
	recebe dois números inteiros e retorna o menor multiplo
	comum entre eles dois.
	'''
	multiplier = 1
	maior = max(n1, n2)
	while n1 > 1 or n2 > 1:
		for i in range(1, maior + 1):
			if n1 % i == 0 and n2 % i == 0 and is_prime(i):
				n1 = n1 / i
				n2 = n2 / i
				multiplier *= i
				break
			elif n1 % i == 0 and is_prime(i):
				n1 = n1 / i
				multiplier *= i
				break
			elif n2 % i == 0 and is_prime(i):
				n2 = n2 / i
				multiplier *= i
				break
	
	return multiplier


print(mmc(5, 10))