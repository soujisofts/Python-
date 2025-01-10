func =  input('Digite o nome deste funcionário: ')
sal = float(input('Digite o salário de {}: '.format(func)))
aum = float(input('Quanto de aumento irá dar para {}: '.format(func)))
res1 = sal / 100
res2 = res1 * aum
res3 = sal + res2

print('O aumento {:.1f}% em {} foi de {:.2f}R$. Logo, O novo salário de {} será exatamente {:.2f}R$.'.format(aum, func, res2, func, res3))

# Retomar explicação do challenge 12, pois a única coisa diferente de desconto e aumento são respectivamente - e + em res3.