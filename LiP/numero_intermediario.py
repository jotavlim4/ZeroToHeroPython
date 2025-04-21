num1, num2, num3 = input().split()
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

if(maior == num1):
    if(menor == num2):
        meio = num3
    else:
        meio = num2
        
elif(maior == num2):
    if(menor == num1):
        meio = num3
    else:
        meio = num1   

else:
	if(menor == num1):
		meio = num2
	else:
		meio = num1

print(menor, meio, maior)