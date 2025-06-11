def recursive_product(num1, num2):
	result = 0
	if num1 == 1:
		return num2
	else:
		recurse = recursive_product(num1 - 1, num2)
		result = num2 + recurse
		return result
		
x, y = int(input()), int(input())
produto = recursive_product(x, y)
print(f"Produto entre {x} e {y}: {produto}")
