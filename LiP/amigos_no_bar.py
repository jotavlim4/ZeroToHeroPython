total = float(input())
amigos = int(input())

novo_total = total + 0.1 * total

print(f"Sem 10% -> R$ {total/amigos:.2f}")
print(f"Com 10% -> R$ {novo_total/amigos:.2f}")
