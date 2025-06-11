def bubble_sort(l):
	for i in range(len(l)):
		for j in range(i + 1):
			if l[i] < l[j]:
				l[i], l[j] = l[j], l[i]
	return l

def is_equal(l1, l2):	
	i = 0
	while i < len(l1):
		if l1[i] != l2[i]:
			return False
		i += 1
	return True

n = int(input())
l = []
for i in range(n):
	number = int(input())
	l.append(number)
new_l = list(l)
new_l = bubble_sort(new_l)

if is_equal(l, new_l):
	print('ELEMENTOS ORDENADOS')
else:
	print('ELEMENTOS NÃO ORDENADOS')