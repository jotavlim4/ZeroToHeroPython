def bs(l):
	for i in range(len(l)):
		for j in range(i + 1):
			if l[i] < l[j]:
				l[i], l[j] = l[j], l[i]

n = int(input())
l = list()

for i in range(n):
	number = int(input())
	l.append(number)

bs(l)

even_len_1 = (len(l))//2
even_len_2 = (len(l))//2 - 1
odd_len = len(l)//2

if len(l) % 2 == 0:
	print(f"Mediana: {(l[even_len_1] + l[even_len_2])/2:.1f}")
else:
	print(f"Mediana: {l[odd_len]:.1f}")

