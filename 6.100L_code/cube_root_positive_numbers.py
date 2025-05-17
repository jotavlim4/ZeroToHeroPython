x = int(input())
for guess in range(x + 1):
    if guess ** 3 == x:
        print(f"the cube root of {x} is {guess}!")
        break
    elif guess ** 3 > x:
        print(f"{x} is not a perfect cube!")
        break
    else: 
        continue