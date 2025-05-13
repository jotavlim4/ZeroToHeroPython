def conta_digitos_impares(n):
    digitos_impares = 0
    digitos_impares_consecutivos = 0
    r_anterior = -1
    while n > 0:
        q = n // 10
        r_atual = n % 10

        if r_atual % 2 == 1:
            digitos_impares += 1
            if r_anterior % 2 == 1 and r_anterior > 0:
                digitos_impares_consecutivos += 1
        
        r_anterior = r_atual
        n = q
    
    return digitos_impares, digitos_impares_consecutivos
    
if __name__ == '__main__':
    n = int(input())
    impares, impares_consecutivos = conta_digitos_impares(n)
    print(f'{n} possui {impares} digitos impares e {impares_consecutivos} digitos impares consecutivos')
