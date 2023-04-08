"""Escreva um programa que pergunte o salario do funcionario e calcule o valor do seu aumento
para salarios superiores a 1250 cakcuke aumento de 10%
e para inferiores ou iguais, o aumento é de 15%"""
print('Saiba qual será seu novo salario com aumento!')
seu = float(input('Digite seu salario:'))
if seu <= 1250:
    novo1 = seu + (seu * 15/100)
    print(f'Quem ganhava R${seu:.2f} passará a ganhar R${novo1:.2f} agora.')
else:
    novo2 = seu + (seu * 10/100)
    print(f'Quem ganhava R${seu:.2f} passará a ganhar R${novo2:.2f} agora.')