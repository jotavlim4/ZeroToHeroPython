n = int(input())

if n == 1:
	print(0)
elif n == 2:
	print(0)
	print(1)
else: 
	first  = 0
	second = 1
	print(first, end = ' ')
	print(second, end = ' ')
	
	count = 0
	while count < n - 2:
		next_value = first + second
		print(next_value, end = ' ')

		first = second
		second = next_value
		count += 1
		
print('')