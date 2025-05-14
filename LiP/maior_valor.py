n = int(input())
maior = menor = number = int(input())
for i in range(n - 1):
	number = int(input())

	if number > maior:
		maior = number

	if number < menor:
		menor = number

print(maior, menor)