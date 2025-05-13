def soma_pares(n):
	'''
	recebe um número inteiro n e
	retorna a soma de todos os pares menores
	ou iguais que n.
	'''
	s = 0
	for i in range(1, n+1):
		if i % 2 == 0:
			s += i
	return s

if __name__ == '__main__':
	n = int(input())
	print(soma_pares(n))
