nota = float(input())
faltas = int(input())

if (nota >= 5 and faltas <= 20 or nota >= 7):
    print('Aprovado')
elif (nota >= 3 and faltas <= 20):
    print('Recuperação')
else:
    print('Reprovado')