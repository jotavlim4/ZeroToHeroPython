N = int(input())
l1 = list()
for i in range(N):
	item = input()
	l1.append(item)

X, Y = int(input()), int(input())
new_l = list()

for i in range(len(l1)):
	if not (len(l1[i]) == X or len(l1[i]) == Y):
		new_l.append(l1[i]) 
print(new_l)