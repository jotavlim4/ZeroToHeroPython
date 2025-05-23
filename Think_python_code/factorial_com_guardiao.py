def factorial(n):
	if not isinstance(n, int):
		print("Factorial is only defined for integers!")
		return None
	elif n < 0:
		print("Factorial is not defined for negatives integers!")
		return None
	elif n == 0: 
		return 1
	else: 
		return n * factorial(n - 1)

