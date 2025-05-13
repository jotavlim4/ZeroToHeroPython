import math

def is_prime(n):
    '''
    recebe um inteiro n e retorna 1 se n for primo
    e retorna 0 se n não for primo
    '''
    if n <= 1:
        return 0
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return 0
    return 1

def conta_primos(n):
    '''
    recebe um inteiro n e verifica a quantidade de primos
    que existem para cada inteiro j no inteiro 1, ..., n
    '''
    s = 0
    for i in range(1, n + 1):
        while i >= 1:
            s += is_prime(i)
            i -= 1
        print(s, end=' ')
        s = 0
    print()

if __name__ == '__main__':
    n = int(input())
    print('Contagem de primos:')
    conta_primos(n)