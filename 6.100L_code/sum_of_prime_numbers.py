# -*- coding: utf-8 -*-

'''
Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to use a for loop that is a primality test nested inside a for loop that
iterates over the odd integers between 3 and 999.
'''

import math

sum_of_primes = 0
is_prime = True
for i in range(3, 1000):
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			is_prime = False
			break
	if is_prime:
		sum_of_primes = sum_of_primes + i
	is_prime = True
print(f"The sum of the primes between 2 and 1000, not included, is {sum_of_primes}")
