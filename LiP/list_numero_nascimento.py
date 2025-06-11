n = int(input())
nascimentos = list()

for i in range(n):
	number = int(input())
	nascimentos.append(number)

largest = nascimentos[0]
dia = 0

for i in range(1, len(nascimentos)):
	total_nascimentos = 0
	for j in range(0, i):
		total_nascimentos += nascimentos[j]

	if total_nascimentos < nascimentos[i]:
		dia = i

if dia == 0:
	print("não há")
else:
	print(f"dia {dia}")