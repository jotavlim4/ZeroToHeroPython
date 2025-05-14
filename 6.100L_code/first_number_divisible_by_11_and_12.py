# -*- coding: utf-8 -*-

'''
Find a positive integer that is divisible by both 11 and 12
'''

x = 1
while True:
	if x % 11 == 0 and x % 12 == 0:
		break # força a saída do laço.
	x = x + 1
print(f"{x} is divisible by 11 and 12!")

# estando dentro de um loop infinito, que é interrompido
# quando o primeiro número com a propriedade procurada é encontrada.
# podemos fazer usando a instração 'break'