import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
listas = [n1, n2, n3, n4]
random.shuffle(listas)
print('A ordem de apresentação será:')
print(listas)