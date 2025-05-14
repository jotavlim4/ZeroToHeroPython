# -*- coding: utf-8 -*-

x = int(input("Type a integer: "))
ans = 0
for i in range(abs(x)):
	ans = ans + abs(x)
print(f"({x})^2 = {ans}")

