quantia = int(input())

nota_50 = quantia // 50
nota_20 = (quantia % 50) // 20
nota_10 = ((quantia % 50) % 20) // 10
nota_5  = (((quantia % 50) % 20) % 10) // 5
nota_2  = ((((quantia % 50) % 20) % 10) % 5) // 2
nota_1  = ((((quantia % 50) % 20) % 10) % 5) % 2

contagem_notas = (nota_50 != 0) + (nota_20 != 0) + (nota_10 != 0) + (nota_5 != 0) + (nota_2 != 0) + (nota_1 != 0)
mensagem = f"{contagem_notas} tipo(s) de nota(s)"
print(mensagem) 