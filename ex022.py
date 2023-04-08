#Desafio 1
nome = str(input('Digite seu nome completo:')).strip()
maiuculas = nome.upper()
minusculas = nome.lower()
total= (len(nome)-nome.count(' '))
first = nome.split()
firsts = first[0]
primeiro = len(firsts)
print(f"""Seu nome é: {nome}.
Seu nome em maiúsculas é: {maiuculas}.
Seu nome em minúsculas é: {minusculas}.
Seu nome tem ao todo: {total} letras.
Seu primeiro nome é {firsts} e ele tem {primeiro} letras.""")