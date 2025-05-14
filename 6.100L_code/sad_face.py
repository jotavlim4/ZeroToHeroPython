where = input("Go left or right? ")
count = 0

while where == "right":
	if count >= 2:
		print(":(")

	where = input("Go left or right? ")
	count += 1
print("You go out!")