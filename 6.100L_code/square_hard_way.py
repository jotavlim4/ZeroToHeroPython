# -*- coding: utf-8 -*-

x = int(input("Type a positive integer: "))
ans = 0
num_iterations = 0 # inicializando a variável
while num_iterations < x:
	ans = ans + x
	num_iterations = num_iterations + 1 # atualizando
print(f"({x})*({x}) = {ans}")

# note que esse código nao funciona para valor negativos.
# pois a condiçao nunca será avalidada como verdadeira e o
# loop nunca é executado e portanto vai exibir 0 como resposta

# uma solução é:
while num_iterations < abs(x):
	ans = ans + abs(x)
	num_iterations = num_iterations + 1
print(f"({x})*({x}) = {ans}")
