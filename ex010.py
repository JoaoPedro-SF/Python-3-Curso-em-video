real= float(input('Quanto dinheiro você tem ná carteira? R$'))
dolar = real / 5.24
euro = real / 5.62
won = real * 248.22
print (f'Com R${real:.2f} você pode comprar:\nUS$ {dolar:.2f}\nKRW {won:.2f}\nEUR {euro:.2f}')