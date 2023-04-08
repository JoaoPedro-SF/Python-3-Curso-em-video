#Escreva um programa que faça o computador "pensar" um número de 0 a 5 e peça para usuario descobrir
from random import randint
from time import sleep

print('-=-' * 20)
print('Irei pensar em número ente 0 e 5. Tente advinhar...')
print('-=-' * 20)

pc = int(randint(0,5)) #fazendo o computador 'pensar'
nu = int(input('Adivinha qual número entre 0 a 5 eu pensei:')) #usuario tentando advinhar
print('PROCESSANDO...')
sleep(3)
if nu==pc:
    print(f'Você Venceu! Eu também pensei no número {pc}.')
else:
    print(f'Você perdeu! O número que eu pensei foi {pc} e não no {nu}.')
