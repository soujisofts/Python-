# SOBRE OPERADORES ARITMETICOS
# Ordem de precedência:
# 1 - () | 2 - ** <-- potência | 3 - *, /, // <-- divisão inteira, % <-- resto da divisão | 4 --> + e -

# Para se calcular uma raiz quadrada, cúbica etc, se usa esta expressão: 4**(1/2) ou 9**(1/3) <-- força dividir dentro do parenteses(ordem de precendencia) e a divisão dentro é basicamente 1 referente ao número fora e /2 ou /3 pra representar raiz quadrada ou cúbica

# dentro do {}, ao usar o .format, pode avançar carecteres ou adicionar com a expressão {:=^10} ficara ====oi==== <-- ficou assim pq oi tem 2 caracteres. {:^5} <-- alinha no meio sem um caractere pós : e antes de ^

# Adendo importante só se usa uma variavel final -- resultado de um calculo por exemplo -- se for usar o valor de dentro posteriormente, caso não, somente colocar dentro do (). Veja no exemplo:

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

print('A Soma é {}'.format(n1+n2))

# exemplo com variaveis:

sb = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2

print('A subtração é {}, o produto é {}, a divisão é {} e a potência é {} '.format(sb, m, d, p))

print('A divisão inteira é {} e o resto é {} '.format(di, r))
# Em caso de número com muitos caracteres se usa {:.3f} ou {:.4f} para limitar. Basicamente, só muda a numeração de dentro. Basta só colocar o valor dentro do {}
# Para não quebrar a linha se usa após o | .format(), | o   end=', '   <-- da continuidade no texto mesmo que exista 2 print sendo executados
# Para quebra dentro da str: '' se usa \n <-- ajuda muito para não ter que ficar criando mais e mais print


