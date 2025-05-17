solution = int(input("Type:\n(1) for solution using 'while loop'\n(2) for solution using 'for loop'\n"))
if solution == 1:
    # initial guess
    guess = 0
    x = int(input("Type a non-negative integer: "))

    # working with negative integers
    is_negative = x < 0
    while guess**2 < x:
        guess += 1

    if guess**2 == x:
        print(f"\nThe square root of {x} is {guess}!")
    else:
        print(f"\nThe integer {x} is not a perfect square!\n")
        if is_negative:
            print(f"Square root of {x} is not defined...\ndo you want to try {-x}?")

else:
    x = int(input("Type a non-negative integer: "))
    if x < 0:
        print("The square root of a negative number is not defined for integers!")
    else:
        for guess in range(x):
            if guess ** 2 == x:
                print(f"The square root of {x} is {guess}!")
                break
            elif guess ** 2 > x:
                print(f"The square root of {x} does not exist!")
                break
            else:
                continue
