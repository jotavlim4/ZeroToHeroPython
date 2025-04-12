number = input()
number = eval(number) - int(eval(number))
if(abs(number) > 0.000001):
    print(True)
else:
    print(False)