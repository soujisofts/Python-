prod = input('Qual o tipo de Produto/Serviço: ')
val = int(input('Quanto vale o(a) {}: '.format(prod)))
desc = int(input('Quanto de desconto você deseja em {}: '.format(prod)))
res1 = val / 100
res2 = res1 * desc
res3 = val - res2

print('O desconto de {}% em {} é de {:.2f}R$. Logo, o valor de {} será de {:.2f}R$.'.format(desc, prod, res2, prod, res3))

# Basicamente, fiz variaveis pra nome do produto(prod), valor da camisa(val) e o desconto que irá ser aplicado(des). Dito isto, fiz somente variaveis de calculo pra um primeiro resultado de divisão por 100 e depois um segundo resultado pra multiplicação com o desconto e por fim um que mostra o resultado final do produto subtraindo com o valor e o calculo do desconto já aplicado. PS: {:.0f} <-- não exibe virgulas pós numero