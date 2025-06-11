def list_of_even_number(n):
	l = [*range(2, n + 1, 2)]
	return l

def summation(l):
	s = 0
	for i in range(len(l)):
		s += l[i]
	return s

n = int(input())
l = list_of_even_number(n)
ans = summation(l)
print(ans)