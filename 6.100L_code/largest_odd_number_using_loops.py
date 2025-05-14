# -*- coding: utf-8 -*-

'''
Write a program that asks the user to input 10
integers, and then prints the largest odd number that was entered. If
no odd number was entered, it should print a message to that effect.
'''

print("Please, type 10 integers: ")

count = 0
count_odds = 0
largest = int(input())

while count < 9: 
	number = int(input())

	if number % 2 == 1:
		count_odds += 1

	if number > largest:
		largest = number

	count += 1

if count_odds:
	print(f"the largest odd number is {largest}!")
else:
	print("No odd number was entered!")
