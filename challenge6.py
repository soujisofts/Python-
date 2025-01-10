n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))

d1 = n1 * 2
d2 = n2 * 2
t1 = n1 * 3
t2 = n2 * 3
r1 = n1 ** (1/2)
r2 = n2 ** (1/2)

print('Sobre o dobro do 1° e 2° número: {} e {}.\nSobre o triplo do 1° e 2° número: {} e {}.\nSobre a raiz quadrada do 1° e 2° número: {:.2f} e {:.2f}'
      .format(d1, d2, t1, t2, r1, r2))
