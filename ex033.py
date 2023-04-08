"""Faça um programa que leia três números e mostre qual é o maior e qual o menor"""
from time import sleep
n1 = int(input('Digite um número:'))
n2 = int(input('Digite segundo número:'))
n3 = int(input('Digite terceiro número:'))
print('PROCESSANDO...')
sleep(1)
if n1 < n2 and n1 < n3:
    print(f'O menor número é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}')
else:
    print(f'O menor número é {n3}')
print('PROCESSANDO...')
sleep(1)
if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
else:
    print(f'O maior número é {n3}')
print('-=-' * 10)
print('FIM')
print('-=-' * 10)

# resolvendo
#forma simples
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
teste = a
if b<a and b<c:
    teste = b
if c<a and c<b:
    teste = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor valor digitado foi {teste}.')
print(f'O maior valor digitado foi {maior}.')
