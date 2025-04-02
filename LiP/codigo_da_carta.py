number = int(input())

# calcula o resto que corresponde ao valor da carta.
# 13 pois de 0 a 12 existem 13 cartas
value = number % 13 

# o naipe da carta é o quociente da divisão.
suit = number // 13

print(f"Valor: {value}, naipe: {suit}")