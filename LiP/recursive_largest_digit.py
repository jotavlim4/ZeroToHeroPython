def count_digts(n):
    digits = 0
    while n > 0:
        n = n // 10
        digits += 1
    return digits 

def recurse_digits(n):
    largest = 0
    d = 10**(count_digts(n)-1)
    if n % d == 0:
        largest = n // d
        return largest
    else:
        digit = n // d
        largest = recurse_digits(n % d)
        if digit > largest:
            largest = digit
        return largest

x = int(input())
x = abs(x)
print(f"O maior dígito é {recurse_digits(x)}")