s = 'abc def eaaejnfkasdandmndfdv '
s_unique = ''
# podemos usar len(s_unique) como forma de contar as letras únicas
# count_unique = 0

for char in s:
    if char not in s_unique and char != ' ':
        s_unique += char
        # count_unique += 1

print(f"Are {len(s_unique)} unique letters in '{s}'")
print('They are: ', end = ' ')
for i in s_unique:
    print(f"'{i}'", ' ' if i == s_unique[len(s_unique) - 1] else ', ', end = '')
print()
