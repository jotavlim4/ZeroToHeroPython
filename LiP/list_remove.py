def remove_value(a, i):
	new_a = a[:]
	new_l = ''
	for j in range(len(new_a)):
		if new_a[j] != new_a[i]:
			new_a[j] = str(new_a[j])
			new_l += new_a[j]
	new_l = [int(new_l[k]) for k in range(len(new_l))]
	return new_l

n = int(input())
l = list()
for i in range(n):
	number = int(input())
	l.append(number)
index = int(input())
l1 = list()
l1 = remove_value(l, index)

if len(l1) == 0:
	print("lista vazia")
else:
	for i in range(len(l1)):
		print(l1[i], end = ' ')
	print('\n')
