print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
from time import sleep
r1 = float(input('Primeiro seguimento:'))
r2 = float(input('Segundo seguimento:'))
r3 = float(input('Terceiro seguimento:'))
sleep(1)
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os seguimentos acima PODEM FORMAR um triângulo')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo')
sleep(1)
print('FIM!')
print('-=' * 20)