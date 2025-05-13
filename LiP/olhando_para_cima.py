def teto(x):
	'''
	recebe um real x e retorna o menor inteiro
	que é maior que x
	'''
	if x == int(x):
		return int(x)
	else:
		return int(x + 1)

if __name__ == '__main__':
	n = int(input())
	for i in range(n):
		x = float(input())
		print(teto(x), end = ' ')

print()