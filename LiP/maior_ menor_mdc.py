largest = smaller = n = int(input())
for i in range(9):
	n = int(input())
	
	if n > largest:
		largest = n

	if n < smaller:
		smaller = n

for divisor in range(smaller, 0, -1):
	if smaller % divisor  == 0 and largest % divisor == 0:
		gcd = divisor
		break

print(largest, smaller, gcd)