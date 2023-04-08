from time import sleep
print('Número Par ou Impar?')
teste = int(input('Digite um número:'))
resto = teste % 2
print("PROCESSANDO...")
sleep(1)
if resto == 0:
    print(f'O número {teste} é Par!')
else:
    print(f'O número {teste} é Impar!')
