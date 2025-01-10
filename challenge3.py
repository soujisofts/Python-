n1 = int(input('Digite o primeiro número que será somado ao segundo: '))
n2 = int(input('Digite o segundo número que será somado ao primeiro: '))
n3 = int(input('Digite o terceiro número que será somado ao segundo: '))

resultado = n1 + n2 + n3

# print ('A soma entre ', n1, 'e', n2, 'e', n3, 'é: ', resultado, '. Correto?' ) <-- maneira antiga de fazer calculo
print ('A soma entre {}, {} e {}  é: {}. Correto?'.format(n1, n2, n3, resultado))

# PS: A expressão int é usada para fazer calculos em variaveis. usa-se anteriormente aos inputs, após isso, criar mais
# uma variavel final e assim usar expressões de calculo para as variaveis anteriores. usar print e dentro do ''
# usar {} e no final de '' usar .format(variavel1, variavel2, variavel3, variavelfinal etc).
# Obs: Sempre se atentar na formula final dos () para não haver erros.