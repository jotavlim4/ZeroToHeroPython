def inicialize_list(n):
	l = list()
	for i in range(n):
		item = int(input())
		l.append(item)
	return l

def recusive_dot_product(u, v, n):
	i = n - 1
	if i == 0:
		return u[i] * v[i]
	else:
		recurse = u[i] * v[i] + recusive_dot_product(u, v, n - 1)
		return recurse

dim = int(input())
v, u = list(), list()
v = inicialize_list(dim)
u = inicialize_list(dim)

print(f"Produto escalar: {recusive_dot_product(u, v, dim)}")