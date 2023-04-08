'''import math
ang = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}, o Cosseno de {cos:.2f}, e a Tangente de {tang:.2f}.')'''

from math import sin, radians, cos, tan
ang = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(ang))
cos  = cos(radians(ang))
tang = tan(radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}, o COSSENO de {cos:.2f}, e a TANGENTE de {tang:.2f}.')
