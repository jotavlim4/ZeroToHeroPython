# -*- coding: utf-8 -*-

'''
Assume you are given a positive integer variable named N. 
Write a piece of Python code that prints hello world on separate lines, 
N times. You can use either a while loop or a for loop.
'''
n = int(input())
for i in range(n):
	print(f"{i + 1:02d}: Hello World!")

