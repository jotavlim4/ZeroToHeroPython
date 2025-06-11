n = int(input())
lista = list()

for i in range(n):
	number = int(input())
	lista.append(number)

ja_visto = list()

for i in lista:
	if i not in ja_visto:
		ja_visto.append(i)

print(ja_visto)