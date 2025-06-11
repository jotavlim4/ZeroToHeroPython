def largest_name(l):
	bigger = l[0]
	index = 0
	for i in range(len(l)):
		if len(bigger) < len(l[i]):
			bigger = l[i]
			index = i
	return index

def smallest_name(l):
	smaller = l[0]
	index = 0
	for i in range(len(l)):
		if len(smaller) > len(l[i]):
			smaller = l[i]
			index = i
	return index

N = int(input())
l = list()

for i in range(N):
	name = input()
	l.append(name)

for i in range(1, len(l)):
	if i % 2 == 1:
		l.pop(largest_name(l))
	else:
		l.pop(smallest_name(l))

print(l[0])