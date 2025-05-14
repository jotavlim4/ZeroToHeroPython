# -*- coding: utf-8 -*-

'''
Write a program that examines three variables—
x, y, and z—and prints the largest odd number among them. If none
of them are odd, it should print the smallest value of the three.
'''

x = int(input())
y = int(input())
z = int(input())

# minha solução:

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
	smallest = min(x, y, z)
	print(smallest)
else:
	if x % 2 == 0:
		largest = max(y, z)
		print(largest)
	elif y % 2 == 0:
		largest = max(x, z)
		print(largest)
	else:
		larges = max(x, y)
		print(largest)

# solução do livro:
answer = min(x, y, z)

if  x % 2 != 0:
	answer = x

if y % 2 != 0 and y > answer:
	answer = y

if z % 2 != 0 and z > answer:
	answer = z

print(answer)

# nessa solução o valor de 'answer' vai sendo atualizado na medida
# em que as condiçoẽs são verdadeiras.
# note que todos os if's são verificados, mas apenas os que as condiçoẽs
# são satisfeitas é que de fato tem o código executado.
# isso é uma estratégia que pode ser aplicada em outros contextos.

# outra forma de resolver esse problema usando expressões condicionais:

print((x if x > z else z) if x > y else (y if y > z else z))

# (x if x > z else z)  -> vai retorna x se x > z caso contrário retorna z
# o resultado disso é retornado caso x > z, caso contrário retorna
# o resultado de  (y if y > z else z)

# um pouco confuso, mas funcional.