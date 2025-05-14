x = int(input())

i = 1 # inicializador
factorial = 1 
while i <= x:
	factorial *= i # multiplicador
	i += 1 # atualizador 

print(f"{x}! is {factorial}")

# o inicializador cria a variável que vai ser utilizada na condição
# o atualizador sempre modifica a variável para que a condição de parada
# seja atingida em algum momento e o loop while possa ser interrompido.