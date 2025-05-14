m = int(input())

if m == 0:
	print('0! = 1')
elif m > 0:
	fatorial = 1
	for i in range(1, m+1):
		fatorial = fatorial * i
		print(f'{i}! = {fatorial}')
else:
	pass
