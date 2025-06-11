def recursive_digits(n):
	if n // 10 == 0:
		print(n % 10)
	else:
		print(n % 10, end = '')
		recursive_digits(n // 10)

x = int(input())
print("Impressao em ordem inversa: ", end = '')
recursive_digits(x)