x = int(input("type a integer: "))
for guess in range(abs(x) + 1):
    if guess ** 3 ==  abs(x):
        if x < 0:
            guess = -guess
            print(f"the cube root of {x} is {guess}!")
            break
        else:
            print(f"the cube root of {x} is {guess}!")
            break
    elif guess ** 3 > abs(x):
        print(f"{x} is not a perfect cube!")
        break
    else: 
        continue
        
