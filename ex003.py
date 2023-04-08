print ('Calcule dois números!')
c1= float(input('Lanche que você comprou:'))
c2= float(input('Bebida que você comprou:'))
soma = (c2 + c1)
texto_soma= f'R${soma:_.2f}'
texto_soma= texto_soma.replace(".",",").replace("_",".")
print (f'Você gastou exatamente {texto_soma }')