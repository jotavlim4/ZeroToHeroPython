# baseado no algoritmo iterativo dado 
# no livro 'discrete mathematics with application, 4ed, susanna epp, p.218-219'

def recursive_remainder(a, d):
	'''
	recebe um inteirno nao negativo a, e um inteiro positivo d
	retorna o resto da divisao inteira de a e d
	'''
	if a == 0:
		return 0
	else:
		if a - d < d:
			return a - d	
		else:
			return recursive_remainder(a - d, d)
		
x, y = int(input()), int(input())
remainder = recursive_remainder(x, y)
print(f"Resto da divisao entre {x} e {y}: {remainder}")