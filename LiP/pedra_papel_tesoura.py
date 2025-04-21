jogador1, jogador2 = input().split()

vencedor = False
empate = False

if(jogador1 == 'r'):
	if(jogador2 == 's'):
		vencedor = True
	elif(jogador2 == 'p'):
		vencedor = False
	else:
		empate = True

elif(jogador1 == 's'):
	if(jogador2 == 'p'):
		vencedor = True
	elif(jogador2 == 'r'):
		vencedor = False
	else:
		empate = True

else:
	if(jogador2 == 'r'):
		vencedor = True
	elif(jogador2 == 's'):
		vencedor = False
	else:
		empate = True

if(vencedor and not empate):
	print('Jogador 1 ganhou')
elif(not vencedor and not empate):
	print('Jogador 2 ganhou')
else:
	print('Empate')