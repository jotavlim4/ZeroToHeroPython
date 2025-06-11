def list_without_rep(l):
	seen = list()
	for i in range(len(l)):
		if l[i] not in seen:
			seen.append(l[i])
	return seen

def count_occurrence(list1, list2):
	count = [0 for i in range(len(list1))]
	for i in range(len(list1)):
		for j in range(len(list2)):
			if list1[i] == list2[j]:
				count[i] += 1 
	return count
		
l = input().split(" ")
l = [int(l[i]) for i in range(len(l))]

occurrence = list_without_rep(l)
count = count_occurrence(occurrence, l)

for i in range(len(occurrence)):
	print(f"{occurrence[i]} = {count[i]}")