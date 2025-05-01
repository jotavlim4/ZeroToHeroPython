n = int(input())

e = 1
for i in range(1, n + 1):
	fatorial = 1
	for j in range(1 , i + 1):
		fatorial = fatorial * j
	e = e + 1/fatorial

print(e)