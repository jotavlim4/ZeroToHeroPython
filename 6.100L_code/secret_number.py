secret_number = int(input("type a interger: "))
found = False
for guess in range(1, 11):
    if guess == secret_number:
        found = True
print("not found!") if not found else print("found!")



