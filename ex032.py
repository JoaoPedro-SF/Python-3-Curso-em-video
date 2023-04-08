# como saber se é ano bissexto
from datetime import date
print('Analise se um ano é BISSEXTO!')
ano = int(input('Que ano quer analisar?:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é BISSEXTO.')