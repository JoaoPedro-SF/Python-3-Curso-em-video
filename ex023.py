num = int(input('Digite um número entre 0 e 99999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
dm = num // 10000 % 10
print(f'analisando o número {num}.')
print(f'Unidade: {u}.')
print(f'Dezena : {d}.')
print(f'Centena: {c}.')
print(f'Milhar : {m}.')
print(f'Dezena de milhar: {dm}')