valor_total = float(input())
valor_recebido = float(input())

troco = valor_recebido - valor_total

troco_notas = int(troco) # pegamos só a parte inteira do troco.
troco_moedas = int((troco - troco_notas) * 100) #multiplicamos por 100 para corresponder a centavos -> 0,50 * 100 = 50 centavos

#troco em notas priorizando notas altas
notas_20 = troco_notas // 20
notas_10 = (troco_notas % 20) // 10
notas_5 = ((troco_notas % 20) % 10) // 5
notas_2 = (((troco_notas % 20) % 10) % 5) // 2
notas_1 = (((troco_notas % 20) % 10) % 5) % 2

#troco em moedas priorizanado moedas mais altas
moedas_50 = troco_moedas // 50
moedas_10 = (troco_moedas % 50) // 10
moedas_5 = ((troco_moedas % 50) % 10) // 5

print(f"Venda: R$ {valor_total:.2f}\nTroco: R$ {troco:.2f}")
print("Para fazer o troco, entregue:")
print(f"R$ 20,00 x {notas_20}") 
print(f"R$ 10,00 x {notas_10}") 
print(f"R$ 5,00 x {notas_5}") 
print(f"R$ 2,00 x {notas_2}") 
print(f"R$ 1,00 x {notas_1}") 
print(f"R$ 0,50 x {moedas_50}") 
print(f"R$ 0,10 x {moedas_10}") 
print(f"R$ 0,05 x {moedas_5}")


