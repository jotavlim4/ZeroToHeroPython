n = int(input())
print(f'A soma dos dígitos de {n} = ', end = '')
s = 0
r = n
while n > 0:
	r = n % 10
	n = n // 10
	s = s + r
print(s)