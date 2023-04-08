print ('Você tem Silva no nome?')
nome = str(input('Digite seu nome completo: '))
no = nome.lower().split()
pro = 'silva' in no
print(f'{pro}')