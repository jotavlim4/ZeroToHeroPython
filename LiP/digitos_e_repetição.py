def contagem_digitos(n):
    number = str(n)
    digits = '0123456789'
    count = 0

    for i in digits:
        for j in number:
            if i == j:
                count += 1
        if count == 0:
            pass
        else:
            print(f'{i} = {count}')
        
        count = 0
        
if __name__ == '__main__':
    number = int(input())
    contagem_digitos(number)