nome = str(input('Digite seu nome:')).upper().strip()
print(f'A letra "A" aparece {nome.count("A")} vezes.')
# O +1 foi usado para aparecer 1 em vez de posição 0
print(f'A primeira letra "A" apareceu na posição {nome.find("A")+1}')
# usar o R para começar a contar da esquerda pra direita que é l
print(f'A ultima letra "A" apareceu na posição {nome.rfind("A")+1}')