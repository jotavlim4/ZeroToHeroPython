import math

def is_prime(n):
    '''
    recebe um inteiro n e retorna 1 se n for primo
    e retorna 0 se n não for primo
    '''
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True

def contagem_fatores_primos(n):
    '''
    recebe um inteiro e executa o algoritmo
    para decompor o número em fatores primos e
    retorna a quantidade de fatores primos.
    '''
    count = 0
    while n > 1:
        for i in range(1, n + 1):
            if n % i == 0 and is_prime(i):
                count += 1
                n = n // i
                break
    
    return count
            
if __name__ == '__main__':
    n = int(input())
    print(f'{n} tem {contagem_fatores_primos(n)} fatores primos')