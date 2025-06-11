def frequent_number(l1, l2, l3, x):
	count = 0
	for i in l1:
		if x in l1:
			count += 1
			break
	for j in l2:
		if x in l2:
			count += 1
			break

	for k in l3:
		if x in l3:
			count += 1
			break

	if count == 2:
		print(f"{x} é um número frequente")
	else:
		print(f"{x} não é um número frequente")


l1 = input().split(' ')
l2 = input().split(' ')
l3 = input().split(' ')
x = int(input())
x = str(x)

frequent_number(l1, l2, l3, x)

