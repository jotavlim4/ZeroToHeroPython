def bs(l):
	for i in range(len(l)):
		for j in range(i + 1):
			if l[i] > l[j]:
				l[i], l[j] = l[j], l[i]


n = int(input())
l = list()

for i in range(len(l)):
	number = int(input())
	l.append(number)

bs(l)

if len(l) % 2 == 0:
	print(f"Mediana: {l[len/2] + l[len/2 -1]}")
else:
	print(f"Mediana: {l[len/2]:.1f}")

