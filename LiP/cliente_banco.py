'''
Ter um nome com mais de 30 letras se tem idade entre 30 e 40,
ou ter renda acima de R$ 1300 se for casado ou viúvo e não for idoso.
'''
elegivel = False

nome = input()
idade = int(input())
estado_civil = input()
renda = int(input())

#remove os espaços para contas apenas as letras do nome
nome = nome.replace(" ", "") 

# Q se P equivale a P => Q q equivale a ~P v Q
P = 30 <= idade <= 40
Q = len(nome) > 30
R = (estado_civil == 'casado' or estado_civil == "viúvo") and (idade < 60)
S = renda > 1300

if(P and Q):
	elegivel = True

if(R and S):
	elegivel = True

if(not(elegivel)):
	elegivel = False

print(elegivel)