def inicialize_list():
	item = None
	l = list()
	while item != 0:
		item = int(input())
		if item == 0:
			break
		else:
			l.append(item)
	return l
			
def largest_dif(l):
	largest = -1 # vai ser um número positivo
	dif = n = m = None
	for i in range(len(l)):
		if i == 0:
			for j in range(1, 2):
				dif = abs(l[i] - l[j])
				if dif > largest:
					largest = dif
					n = i
					m = j
		elif i < len(l) - 1:
			for j in range(i-1, i+2):
				dif = abs(l[i] - l[j])
				if dif > largest:
					largest = dif
					n = i
					m = j
		else:
			for j in range(len(l)-1, len(l)-2, -1):
				dif = abs(l[i] - l[j]) 
				if dif > largest:
					largest = dif
					n = i
					m = j
	return largest, l[n], l[m]

vec = inicialize_list()
lar, x, y = largest_dif(vec)
print(f"{y} e {x}, cuja subtração em módulo é {lar}.")
