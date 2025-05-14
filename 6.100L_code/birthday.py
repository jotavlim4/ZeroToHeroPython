# -*- coding: utf-8 -*-

'''
Write code that asks the user to enter their
birthday in the form mm/dd/yyyy, and then prints a string of the
form ‘You were born in the year yyyy.’
'''

answer = input("Type your birthday in the form mm/dd/yyyy: ")
year = answer[6:len(answer)]
print(f"You were born in the year {year}.")

