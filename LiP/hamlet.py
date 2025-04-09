print("b", "2b or not 2b", sep = '\t')

b = False
print(f"{b}", f"{b or not b}", sep = '\t')
b = True
print(f"{b}", f"{b or not b}", sep = '\t')