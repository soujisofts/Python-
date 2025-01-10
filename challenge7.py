nomealuno = input('Digite o nome do aluno: ')
n1 = float(input('Digite a 1° Nota: '))
n2 = float(input('Digite a 2° Nota: '))
n3 = float(input('Digite a 3° Nota: '))
n4 = float(input('Digite a 4° Nota: '))
m = (n1 + n2 + n3 + n4) / 4

print('A média final do aluno(a) {} é de {:.1f}'.format(nomealuno, m))
# Outra maneira de fazer é colocando o f antes do '' e a variavel dentro do {}. Caso, não ira usar posterirormente.