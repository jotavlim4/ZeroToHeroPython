number = int(input())

true_out = 'Numero é formado apenas por 0s e 1s'
false_out = 'Numero não é formado apenas por 0s e 1s'
ones_and_zeros = False

r = 0
while number > 0:
	r = number % 10
	if r == 0 or r == 1:
		ones_and_zeros = True
	else:
		ones_and_zeros = False
		break
	number = number // 10

if ones_and_zeros:
	print(true_out)
else:
	print(false_out)

