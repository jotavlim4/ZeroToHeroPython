def soma_multiplos_3(a, b):
	'''
	recebe dois inteiros a e b 
	retorna a soma dos multiplos de 3 que 
	existem no intervalo discreto [a, b]
	'''
	s = 0
	for i in range(a, b+1):
		if i % 3 == 0:
			s += i
	return s

def maior_soma(a, b, c, d):
	'''
	recebe 4 inteiros que correspondem as extremidades de dois intervalos
	discretos, calcula a soma dos múltiplos de 3 em cada intervalo e 
	retorna o intervalo que tem a maior soma e o valor da soma.
	'''
	s1 = soma_multiplos_3(a, b)
	s2 = soma_multiplos_3(c, d)

	if s1 > s2:
		print(f'Intervalo 1: {s1}')
	elif s1 == s2:
		print(f'Iguais: {s1}')
	else:
		print(f'Intervalo 2: {s2}')

if __name__ == '__main__':
	x1 = int(input())
	x2 = int(input())
	y1 = int(input())
	y2 = int(input())
	maior_soma(x1, x2, y1, y2)

