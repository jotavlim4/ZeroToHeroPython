# verify if a integer x is a perfect square

# initial guess
guess = 0
x = int(input('Type a integer: '))

# exit loop when guess ** 2 >= x
# guess ** 2 == x, we found a perfect square
# guess ** 2 > x, we don't found a perfect square
# don't work for negatives x's
while guess ** 2 < x:
    guess += 1

if guess ** 2 == x:
    print(f"{x} is a perfect square and it square is {guess}")
else:
    print(f"{x} is not a perfect square")
