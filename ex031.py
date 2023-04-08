"""Desenvolva um programa que pergunte a distância de uma viagem em km.
Caulcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas"""
distancia = int(input('Qual a distância em km até o seu destino?:'))

if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45
print(f'Sua passagem custará R${preço:.2f}.')