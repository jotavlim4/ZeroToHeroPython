# -*- coding: utf-8 -*-

'''
Replace the comment in the following code with a
while loop.
'''

num_x = int(input())
to_print = '' # string vazia
count = 0 # inicializando um contador

#concatenate X to to_print num_x times
while count < num_x:
	to_print += 'X'
	count += 1
print(f"'X' {num_x} times: {to_print}") 