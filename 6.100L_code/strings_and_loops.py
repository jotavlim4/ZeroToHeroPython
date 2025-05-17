s = 'joao victor lima da silva'
s_upper = ''
# transforma uma string lowercase em uppercase
# usando indices:
for i in range(len(s)):
    if  'a' <= s[i] <= 'z':
        s_upper += chr(ord(s[i]) - 32)
    else:
        s_upper += s[i] # adiciona os espaços
print(s_upper)

s_upper = ''
# usando a própria string como sequencia:
for char in s:
    if 'a' <= char <= 'z':
        s_upper += chr(ord(char) - 32)
    else:
        s_upper += char
print(s_upper)

s_upper = ''
# usando a própria string como sequencia:
# usando método lower()
for char in s:
    s_upper += char.upper()
print(s_upper)
