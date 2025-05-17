x = int(input())
for guess in range(abs(x) + 1):
    if guess ** 3 >= abs(x):
        break
if guess ** 3 != abs(x):
    print(f"{x} is not a perfect cube!")
else:
    if x < 0:
        guess = -guess
        print(f"the cube root of {x} is {guess}!")
    else:
        print(f"the cube root of {x} is {guess}!")