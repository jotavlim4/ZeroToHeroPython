'''
Assume 3 variables are already defined for you: a, b, and c. 
Create a variable called total that adds a and b then multiplies the result by c. 
Include a last line in your code to print the value: print(total)
'''

# atribuição usado linha por linha
a = 1
b = 2
c = 9
total = (a + b) * c
print(total) #27

# usando atribuição multipla

a, b, c = 1, 2, 9 # se eu não estou errado, vi em algum lugar que isso se chama 'tupla'
total = (a + b) * c
print(total) #27