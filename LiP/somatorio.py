b = int(input())

s = 0
for i in range(1, b + 1):
	s = s + (i)**(1/i)

print(s)