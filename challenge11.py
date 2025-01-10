l1 = int(input('Digite a Largura em metros da sua parede: '))
a1 = int(input('Digite a Altura em metros da sua parede: '))
ar = l1 * a1
tinta = ar // 2

print(f'A área corresponde a {ar}m² \nE serão necessários {tinta}L de tinta.')


# Basicamente, fiz o calculo da seguinte maneira: multipliquei altura e largura em uma variavel pra descobrir a area --> ar = l1 * a1 <-- e dividi o resultado disso por 2 em uma nova variavel pra saber o tanto de tinta --> tinta = ar // 2 <--

