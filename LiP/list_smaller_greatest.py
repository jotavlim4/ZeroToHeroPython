def inicialize_list(n):
	l = list()
	for i in range(n):
		item = float(input())
		l.append(item)
	return l

def smallest(l):
	smaller = l[0]
	for i in range(len(l)):
		if smaller > l[i]:
			smaller = l[i]
	return smaller

def largest(l):
	bigger = l[0]
	for i in range(len(l)):
		if bigger < l[i]:
			bigger = l[i]
	return bigger

def func(l1 , l2):
	return smallest(l1) > largest(l2)

n1 = int(input())
a = inicialize_list(n1)
n2 = int(input())
b = inicialize_list(n2)

print(f'Saída "{func(a, b)}"')