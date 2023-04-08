"""Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h
mostre mensagem dizendo que ele foi multado. A mulkta vai custar R$7,00 por cada km acima do limite"""
from time import sleep
velo = int(input('Quantos quilometros por hora você passou?:'))
print('PROCESSANDO...')
sleep(1)
if velo>=81:
    valor = (velo - 80) * 7
    print(f'MULTADO! Você excedeu o limite de 80km/h dessa estrada! \nTerá de pagar uma multa de R${valor:.2f} reais.')
else:
    print('Você andou dentro do limite maximo dá estrada que é de 80km/h. \nTenha um bom dia e dirija com segurança!')
